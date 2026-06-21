def reverse_words(s):
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_string = "  The   quick brown fox jumps over the lazy dog  "
    result = reverse_words(sample_string)
    print(result)