def get_first_letters(strings):
    if not isinstance(strings, list):
        raise ValueError("Input must be a list of strings.")
    return [s[0] for s in strings if s]

if __name__ == '__main__':
    sample_values = ["kiwi", "mango", "papaya", "grape"]
    try:
        result = get_first_letters(sample_values)
        print(result)
    except ValueError as e:
        print(e)