def reverse_word(word):
    if not isinstance(word, str):
        raise ValueError("Input must be a string")
    
    reversed_chars = []
    for char in word:
        reversed_chars.insert(0, char)
    
    return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_values = ["Python", "", "a", "Alibaba Cloud"]
    for value in sample_values:
        print(reverse_word(value))