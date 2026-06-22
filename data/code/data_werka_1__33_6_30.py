def remove_spaces_from_strings(strings):
    return [s.replace(" ", "") for s in strings]

if __name__ == '__main__':
    sample_input = ["hello world", "python programming", "remove spaces"]
    result = remove_spaces_from_strings(sample_input)
    print(result)