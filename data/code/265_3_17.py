def separate_even_odd_chars(phrase):
    if not isinstance(phrase, str):
        raise ValueError("Input must be a string")
    
    even_chars = ''.join(char for char in phrase if ord(char) % 2 == 0)
    odd_chars = ''.join(char for char in phrase if ord(char) % 2 != 0)
    return even_chars, odd_chars

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    try:
        even, odd = separate_even_odd_chars(sample_phrase)
        print("Even ASCII value characters:", even)
        print("Odd ASCII value characters:", odd)
    except ValueError as e:
        print(e)