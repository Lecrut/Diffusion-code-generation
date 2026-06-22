def get_last_item(items):
    if not items:
        raise ValueError("The list is empty.")
    return items[-1]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    try:
        last_element = get_last_item(sample_list)
        print(f"The last item in the list {sample_list} is: {last_element}")
    except ValueError as e:
        print(e)