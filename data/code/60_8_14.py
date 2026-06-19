def get_last_item(string_list):
    if string_list:
        return string_list[-1]
    else:
        return None

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    last_item = get_last_item(sample_list)
    print(f"The last item in the list is: {last_item}")