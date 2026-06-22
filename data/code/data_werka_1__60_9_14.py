def get_last_item(string_list):
    if not string_list:
        raise ValueError("The list is empty.")
    return string_list[-1]

if __name__ == '__main__':
    SAMPLE_LIST = ["apple", "banana", "cherry", "date"]
    try:
        last_item = get_last_item(SAMPLE_LIST)
        print("The list of strings is:", SAMPLE_LIST)
        print("The last item in the list is:", last_item)
    except ValueError as e:
        print(e)