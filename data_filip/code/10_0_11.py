def reverse_words(s):
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample = "hello world from python"
    print(reverse_words(sample))