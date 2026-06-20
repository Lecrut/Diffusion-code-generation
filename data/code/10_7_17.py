def reverse_words(sentence: str) -> str:
    words = sentence.split()
    reversed_words = []
    for i in range(len(words) - 1, -1, -1):
        reversed_words.append(words[i])
    return ' '.join(reversed_words)

if __name__ == '__main__':
    print(reverse_words("Hello World from Python"))