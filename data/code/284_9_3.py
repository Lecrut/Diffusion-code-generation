def reverse_words_in_string(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_input = "Python is fun to learn"
    result = reverse_words_in_string(sample_input)
    print(result)