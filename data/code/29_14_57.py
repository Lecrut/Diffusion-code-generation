def reverse_word(word):
    if not isinstance(word, str):
        raise ValueError("Input must be a string")
    if len(word) <= 1:
        return word
    return word[-1] + reverse_word(word[:-1])

if __name__ == '__main__':
    sample_values = ["hello", "", "a", "Qwen"]
    for value in sample_values:
        print(reverse_word(value))