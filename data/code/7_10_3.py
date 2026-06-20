import re

def contains_special_characters(text):
    if not isinstance(text, str):
        return False
    return bool(re.search(r'[^a-zA-Z0-9]', text))

if __name__ == '__main__':
    sample_text = "Hello World!"
    result = contains_special_characters(sample_text)
    print(result)
    
    sample_text_no_special = "HelloWorld123"
    result_no_special = contains_special_characters(sample_text_no_special)
    print(result_no_special)