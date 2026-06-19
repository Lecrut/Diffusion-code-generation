def count_repeated_letters(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    letter_count = {}
    for char in s:
        if char.isalpha():
            char_lower = char.lower()
            letter_count[char_lower] = letter_count.get(char_lower, 0) + 1
    
    repeated_letters = {char: count for char, count in letter_count.items() if count > 1}
    return repeated_letters

if __name__ == '__main__':
    sample_string = "Hello World! This is a Test String with some Repeated letters."
    try:
        result = count_repeated_letters(sample_string)
        print(result)
    except ValueError as e:
        print(e)