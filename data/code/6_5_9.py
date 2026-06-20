def process_string(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    original_text = "hello world example"
    result = process_string(original_text)
    print(result)