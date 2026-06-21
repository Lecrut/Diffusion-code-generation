def reverse_words(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    words = text.split()
    return " ".join(reversed(words))

if __name__ == '__main__':
    sample_string = "Hello World from Python"
    print(f"Input: '{sample_string}'")
    print(f"Output: '{reverse_words(sample_string)}'")