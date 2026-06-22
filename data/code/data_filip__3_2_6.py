import re

def remove_vowels(input_string: str) -> str:
    result = re.sub(r'[aeiouAEIOU]', '', input_string)
    return result

if __name__ == '__main__':
    sample_text = "Hello World"
    output = remove_vowels(sample_text)
    print(output)