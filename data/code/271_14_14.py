import re

def remove_vowels(text):
    vowels = 'aeiouAEIOU'
    pattern = f"[{re.escape(vowels)}]"
    return re.sub(pattern, '', text)

if __name__ == '__main__':
    sample_text = "Python Programming!"
    result = remove_vowels(sample_text)
    print(result)