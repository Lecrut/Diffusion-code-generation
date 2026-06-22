def remove_spaces(strings):
    if not all(isinstance(item, str) for item in strings):
        raise ValueError("All elements in the list must be strings.")
    return [item.replace(" ", "") for item in strings]

if __name__ == '__main__':
    sample_strings = ["Hello World", "This is a test string", "Spaces here"]
    result = remove_spaces(sample_strings)
    print(result)