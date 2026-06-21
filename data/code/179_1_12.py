def reverse_words(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    words = text.split()
    return " ".join(words[::-1])

if __name__ == '__main__':
    test_string = "Hello World from Python"
    print(f"Input: '{test_string}'")
    print(f"Output: '{reverse_words(test_string)}'")