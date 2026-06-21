def get_last_item(string_list):
    if not string_list:
        raise ValueError("The list is empty")
    return string_list[-1]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    last_item = get_last_item(sample_list)
    print(f"The last item in the list is: {last_item}")