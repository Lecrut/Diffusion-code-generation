import re

def isolate_punctuation(input_string):
    return re.sub(r'([^\w\s])', r'\1 ', input_string)

if __name__ == '__main__':
    sample_input = "Hello, world! How are you?"
    print(isolate_punctuation(sample_input))