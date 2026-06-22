def get_first_letters(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    words = text.split()
    return [word[0] for word in words if word]

if __name__ == '__main__':
    sample_string = "An example with different words"
    try:
        result = get_first_letters(sample_string)
        print(result)
    except ValueError as e:
        print(e)