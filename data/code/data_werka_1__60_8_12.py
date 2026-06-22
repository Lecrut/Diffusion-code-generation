def get_last_item(items):
    if not isinstance(items, list):
        raise TypeError("Input must be a list")
    if len(items) == 0:
        raise ValueError("List cannot be empty")
    return items[-1]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    try:
        last_item = get_last_item(sample_list)
        print(f"The last item in the list is: {last_item}")
    except (TypeError, ValueError) as e:
        print(e)