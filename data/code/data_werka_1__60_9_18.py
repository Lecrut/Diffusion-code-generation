def validate_input(input_list):
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    if not input_list:
        raise ValueError("The list is empty")

def get_last_item(string_list):
    validate_input(string_list)
    return string_list[-1]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date", "elderberry"]
    try:
        last_item = get_last_item(sample_list)
        print("The list of strings is:", sample_list)
        print("The last item in the list is:", last_item)
    except (TypeError, ValueError) as e:
        print(e)