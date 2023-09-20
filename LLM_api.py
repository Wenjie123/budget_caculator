import streamlit as st
import pandas as pd

def LLM_price(LLM_name: str, input_token, output_token,  training_tokens, time, rl_time):
    """

    :param LLM_name:  the name of LLM
    :param output_token:
    :param input_token:
    :param training_tokens: the tokens used in training process
    :param time: finetune time
    :param rl_time: the time used in training Reinforcement learning
    :return: total price of LLM
    """
    if LLM_name == "GPT4-8k":
        price = (0.03 / 1000) * input_token + (0.06 / 1000) * output_token
    elif LLM_name == "GPT-32k":
        price = (0.06 / 1000) * input_token + (0.12 / 1000) * output_token
    elif LLM_name == "GPT3.5-4k":
        price = (0.0015 / 1000) * input_token + (0.002 / 1000) * output_token
    elif LLM_name == "GPT3.5-16k":
        price = (0.003 / 1000) * input_token + (0.004 / 1000) * output_token
    elif LLM_name == "Claude-Instant":
        price = (1.63 / 10**6) * input_token
    elif LLM_name == "Claude2":
        price = (11.02 / 10**6) * input_token
    elif LLM_name == "ChatGLM-Pro":
        price = (0.01 / 1000) * input_token
    elif LLM_name == "ERNIE":
        price = (0.012 / 10000) * input_token
    elif LLM_name == "qwen-plus":
        price = (0.14/ 10000) * (input_token - 1000000)
    elif LLM_name == "GPT3.5-finetune":
        price = (0.008 / 1000) * training_tokens + (0.012/1000) * input_token + (0.016/1000) * output_token
    elif LLM_name == "LLama2-70b":
        price = 16 * 9 * time + 96 * 2 * time

    total_price = price + (8 * 9 + 0.08 * 128) * rl_time
    return round(total_price, 1)


def price_table(input_tokens=100*1e9, output_tokens=300*1e9, training_tokens=100*1e9, finetune_time=15.0, rl_time=30.0*24):
    LLM_lists = ["GPT4-8k", "GPT-32k", "GPT3.5-4k", "GPT3.5-16k", "Claude-Instant", "Claude2", "ChatGLM-Pro", "ERNIE", "qwen-plus", "GPT3.5-finetune",
                 "LLama2-70b"]

    all_price = dict()
    all_price["大模型"] = "除了GPT系列和Claude系列的单位为美元，其余单位为人名币"

    for item in LLM_lists:
        single_price = LLM_price(item, output_tokens, input_tokens, training_tokens, finetune_time, rl_time)
        all_price[item] = single_price

    # all_prices = pd.DataFrame(all_price)
    return all_price


def main():
    text = "目前考虑的大模型都是各个厂家的大模型顶配版(价格最贵的版本)。"
    st.title("大模型及其相关预算")
    st.text(text)

    input_tokens = st.number_input("Please enter the number of input tokens", value=100*1e9)
    output_tokens = st.number_input("Please enter the number of output tokens", value=300*1e9)
    training_tokens = st.number_input("Please enter the number of training tokens", value=100*1e9)
    finetune_time = st.number_input("Please enter the time of finetune time(hours)", value=15)
    RL_time = st.number_input("Please enter the Reinforcement learning time(hours)", value=30 * 24)

    data = price_table(input_tokens, output_tokens, training_tokens, finetune_time, RL_time)
    st.table(data)
    st.text("从上面的表格中可以看到微调LLaMa2-70b是价格最划算的方案， 但可能在最终效果上未必有调GPT4 API的效果好。")


if __name__ == "__main__":
    main()
