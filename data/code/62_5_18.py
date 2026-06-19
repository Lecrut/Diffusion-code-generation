def get_second_string(strings):
    if len(strings) < 2:
        raise ValueError("The list must contain at least two elements.")
    return strings[1]

if __name__ == '__main__':
    sample_strings = ["first", "second", "third"]
    print(get_second_string(sample_strings))