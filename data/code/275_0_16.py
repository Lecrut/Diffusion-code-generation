def to_uppercase(strings):
    uppercased = []
    for s in strings:
        uppercased.append(s.upper())
    return uppercased

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    result = to_uppercase(sample_strings)
    for upper_string in result:
        print(upper_string)