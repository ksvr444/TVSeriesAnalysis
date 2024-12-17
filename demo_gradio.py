import gradio as gr

def analyze_sentiment(sentence):
    if "good" in sentence:
        return "positive"
    elif "bad" in sentence:
        return "negative"
    else:
        return "neutral"

with gr.Blocks() as app:
     with gr.Row():
            with gr.Column():
                gr.HTML("<h1>Theme Classification (Zero Shot Claasifiers)</h1>")
                with gr.Row():
                    with gr.Column():
                        sentimentkjsd = gr.Label()
                    with gr.Column():
                        sentence = gr.Textbox()
                        sentiment = gr.Label()
                        submit = gr.Button()

                        submit.click(fn=analyze_sentiment,
                                    inputs=sentence,
                                    outputs=sentimentkjsd)

app.launch()