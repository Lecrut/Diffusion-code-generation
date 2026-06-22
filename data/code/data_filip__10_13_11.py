import re

def reverse_words(sentence: str) -> str:
    words = re.findall(r'\S+', sentence)
    spaces = re.findall(r'\s+', sentence)
    reversed_words = words[::-1]
    result = []
    for i, word in enumerate(reversed_words):
        result.append(word)
        if i < len(spaces):
            result.append(spaces[i])
    return ''.join(result)

if __name__ == '__main__':
    print(reverse_words("Hello  world"))