def get_last_string(string_list):
    if not string_list:
        return None
    return string_list[-1]
if __name__ == '__main__':
    my_list = ["apple", "banana", "cherry", "date"]
    last_item = get_last_string(my_list)
    print("The list of strings is:", my_list)
    print("The last item in the list is:", last_item)