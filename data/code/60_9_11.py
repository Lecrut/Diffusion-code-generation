def get_last_item(input_list):
    if not input_list:
        raise ValueError("The list is empty.")
    return input_list[-1]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date", "elderberry"]
    try:
        last_element = get_last_item(sample_list)
        print("The list of strings is:", sample_list)
        print("The last item in the list is:", last_element)
    except ValueError as e:
        print(e)