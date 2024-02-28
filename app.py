import gradio as gr
import pandas as pd
import random

def random_excel_viewer(excel_file):
    df = pd.read_excel(excel_file.name)
    column_name = df.columns[0]
    random_entry = random.choice(df[column_name])
    return f"被随机的幸运观众：\n{random_entry}"

iface = gr.Interface(
    fn=random_excel_viewer,
    inputs="file",
    outputs="text",
    layout="vertical",
    title="课堂开心点名器",
    description="随机抽取一名幸运观众。"
)

iface.launch()

# 运行主循环
root.mainloop()