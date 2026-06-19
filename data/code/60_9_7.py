def get_last_item(lst):
    if not lst:
        raise ValueError("The list is empty.")
    return lst[-1]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    try:
        last_item = get_last_item(sample_list)
        print(f"The list of strings is: {sample_list}")
        print(f"The last item in the list is: {last_item}")
    except ValueError as e:
        print(e)

    empty_list = []
    try:
        last_item = get_last_item(empty_list)
        print(f"The list of strings is: {empty_list}")
        print(f"The last item in the list is: {last_item}")
    except ValueError as e:
        print(e)