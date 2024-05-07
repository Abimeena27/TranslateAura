from flask import Flask, render_template, request,jsonify
import boto3

app=Flask(__name__)

def translation(input,source,target):
    client=boto3.client("translate",region_name="ap-south-1")
    response=client.translate_text(
        Text=input,
        SourceLanguageCode=source,
        TargetLanguageCode=target
    )
    result=response['TranslatedText']
    return result

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/translate',methods=['POST'])
def translate():
    data=request.get_json()
    print("REcieved:",data)
    text=data['text']
    source_language=data['source_language_code']
    target_language=str(data.get('target_language_code', ''))
    print("target",target_language)
    result=translation(text,source_language,target_language)
    return jsonify({'result':result})


if __name__=="__main__":
    app.run(debug=True)