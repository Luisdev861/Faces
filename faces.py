emoticon=("🙂")
emoticon2=("🙁")

def convert(text):
    text=text.replace(":)",emoticon)
    text=text.replace(":(",emoticon2)
    return text

def main():
    user_input= input()
    result=convert(user_input)
    print(result)
main()

input()