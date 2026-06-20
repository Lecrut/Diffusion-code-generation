def process_string(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_text = "hello world example"
    result = process_string(sample_text)
    print(result)