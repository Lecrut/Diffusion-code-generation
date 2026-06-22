import re

def remove_vowels(text):
    pattern = r'[aeiouAEIOU]'
    result = re.sub(pattern, '', text)
    return result

if __name__ == '__main__':
    sample_text = "Hello World 1234"
    result = remove_vowels(sample_text)
    print(result)