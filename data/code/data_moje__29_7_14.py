def _is_valid_string(value):
    if not isinstance(value, str):
        raise TypeError("Input must be a string")
    return True

def count_vowels(text):
    _is_valid_string(text)
    vowel_set = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    total = 0
    for character in text:
        if character in vowel_set:
            total += 1
    return total

if __name__ == '__main__':
    test_input = "Programming is fun and creative"
    output = count_vowels(test_input)
    print(output)