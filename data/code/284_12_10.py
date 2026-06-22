def reverse_words(input_string):
    words = input_string.split()
    if not words:
        return ""
    reversed_words = []
    for word in words:
        if not word.strip():
            continue
        reversed_words.append(word[::-1])
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_input = "Hello world from Python"
    result = reverse_words(sample_input)
    print(result)