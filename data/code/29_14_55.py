def is_valid_string(word):
    return isinstance(word, str)

def reverse_word(word):
    if not is_valid_string(word):
        raise ValueError("Input must be a string")
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    return reversed_word

if __name__ == '__main__':
    sample_values = ["world", "", "z", "Qwen"]
    for value in sample_values:
        print(reverse_word(value))