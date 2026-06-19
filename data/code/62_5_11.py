def validate_string_list(strings):
    if len(strings) < 2:
        raise ValueError("The list must contain at least two elements.")

def get_second_string(strings):
    validate_string_list(strings)
    return strings[1]

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    try:
        second_string = get_second_string(sample_strings)
        print(second_string)
    except ValueError as e:
        print(e)