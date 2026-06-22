def reverse_words(s: str) -> str:
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    print(reverse_words("Hello world"))
    print(reverse_words("Python is great"))
    print(reverse_words(""))
    print(reverse_words("Single"))