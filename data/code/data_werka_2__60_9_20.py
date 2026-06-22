def get_last_item(lst):
    if not lst:
        raise ValueError("The list is empty")
    return lst[-1]

if __name__ == '__main__':
    sample_lists = {
        "numbers": [10, 20, 30, 40, 50],
        "alphabets": ['a', 'b', 'c', 'd'],
        "empty": []
    }
    for name, lst in sample_lists.items():
        try:
            last_item = get_last_item(lst)
            print(f"The list '{name}' is: {lst}")
            print(f"The last item in the list '{name}' is: {last_item}")
        except ValueError as e:
            print(e)