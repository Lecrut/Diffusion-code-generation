def reverse_word(word):
    if not isinstance(word, str):
        raise ValueError("Input must be a string")
    
    def validate_input(w):
        if len(w) < 0:
            raise ValueError("Input string length cannot be negative")
    
    validate_input(word)
    
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    return reversed_word

if __name__ == '__main__':
    sample_values = ["hello", "", "a", "Alibaba Cloud"]
    for value in sample_values:
        print(reverse_word(value))