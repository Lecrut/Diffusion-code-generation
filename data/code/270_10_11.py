def remove_spaces(strings):
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements in the list must be strings")
    return [s.replace(' ', '') for s in strings]

if __name__ == '__main__':
    sample_strings = ["Hello World", "Python Programming", "Remove Spaces"]
    try:
        result = remove_spaces(sample_strings)
        print(result)
    except ValueError as e:
        print(e)