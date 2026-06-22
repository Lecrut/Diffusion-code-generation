def remove_spaces_from_strings(strings):
    return [s.replace(" ", "") for s in strings]

if __name__ == '__main__':
    sample_values = ["Hello World", "Python Programming", "Remove Spaces"]
    result = remove_spaces_from_strings(sample_values)
    print(result)