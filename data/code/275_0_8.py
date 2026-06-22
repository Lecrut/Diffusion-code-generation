def uppercase_strings(strings):
    return [s.upper() for s in strings]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    uppercased_list = uppercase_strings(sample_list)
    for item in uppercased_list:
        print(item)