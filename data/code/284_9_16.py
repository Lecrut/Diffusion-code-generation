def reverse_words_in_string(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    words = input_string.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_input = "Python is fun to learn"
    try:
        result = reverse_words_in_string(sample_input)
        print(result)
    except ValueError as e:
        print(e)