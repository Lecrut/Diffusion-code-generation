def reverse_word(word):
    if not isinstance(word, str):
        raise ValueError("Input must be a string")
    return word[::-1]

if __name__ == '__main__':
    sample_word = "optimization"
    try:
        reversed_word = reverse_word(sample_word)
        print(reversed_word)
    except ValueError as e:
        print(e)