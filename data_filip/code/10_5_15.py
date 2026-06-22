import re

def reverse_words(sentence):
    words = re.findall(r'\S+', sentence)
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    print(reverse_words("Hello   World"))
    print(reverse_words("  Python  is  great  "))
    print(reverse_words("One"))
    print(reverse_words("  "))