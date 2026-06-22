def get_last_item(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    if len(lst) == 0:
        raise IndexError("The list is empty and has no last item.")
    return lst[-1]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    try:
        last_item = get_last_item(sample_list)
        print(f"The last item in the list is: {last_item}")
    except Exception as e:
        print(e)