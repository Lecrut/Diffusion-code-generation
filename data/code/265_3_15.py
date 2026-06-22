def validate_input(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    if len(input_string) == 0:
        raise ValueError("Input string cannot be empty")

def separate_by_ascii_value(phrase):
    validate_input(phrase)
    even_chars = ''.join(char for char in phrase if ord(char) % 2 == 0)
    odd_chars = ''.join(char for char in phrase if ord(char) % 2 != 0)
    return even_chars, odd_chars

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    try:
        even, odd = separate_by_ascii_value(sample_phrase)
        print(even)
        print(odd)
    except ValueError as e:
        print(f"Error: {e}")