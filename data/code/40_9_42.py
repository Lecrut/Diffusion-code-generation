def get_first_letters(strings):
    if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
        raise ValueError("Input must be a list of strings.")
    return [s[0] for s in strings if s]

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry", "date"]
    try:
        result = get_first_letters(sample_values)
        print(result)
    except ValueError as e:
        print(e)