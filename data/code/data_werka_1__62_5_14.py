def get_second_string(strings):
    if len(strings) < 2:
        raise ValueError("The list must contain at least two elements.")
    return strings[1]

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry"]
    try:
        second_value = get_second_string(sample_values)
        print(second_value)
    except ValueError as e:
        print(e)