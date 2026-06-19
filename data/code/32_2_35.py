def calculate_length(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    return len(text)

if __name__ == '__main__':
    try:
        sample_string = 'Hello World'
        length_of_string = calculate_length(sample_string)
        print(length_of_string)
    except ValueError as e:
        print(e)