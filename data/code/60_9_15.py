def get_last_item(string_list):
    if not string_list:
        raise ValueError("The list is empty.")
    return string_list[-1]

if __name__ == '__main__':
    sample_list = ["kiwi", "mango", "papaya"]
    try:
        last_element = get_last_item(sample_list)
        print("The list of strings is:", sample_list)
        print("The last item in the list is:", last_element)
    except ValueError as e:
        print(e)