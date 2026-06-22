from collections import deque

def reverse_words(s: str) -> str:
    words = s.split()
    d = deque(words)
    result_words = []
    while d:
        result_words.append(d.pop())
    return ' '.join(result_words)

if __name__ == '__main__':
    print(reverse_words("Hello World"))
    print(reverse_words(""))
    print(reverse_words("   "))
    print(reverse_words("a"))
    print(reverse_words("  hello   world  "))
    print(reverse_words("one two three four"))