def get_second_string(strings):
    if len(strings) < 2:
        raise ValueError("The list must contain at least two elements.")
    return strings[1]

if __name__ == '__main__':
    sample_input = ["first", "second", "third"]
    try:
        result = get_second_string(sample_input)
        print(result)
    except ValueError as e:
        print(e)