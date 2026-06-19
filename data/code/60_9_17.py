def get_last_item(string_list):
    if not string_list:
        raise ValueError("The list is empty.")
    return string_list[-1]

if __name__ == '__main__':
    sample_lists = [
        ["apple", "banana", "cherry", "date"],
        [],
        [1, 2, 3, 4, 5],
        ['a', 'b', 'c']
    ]

    for i, lst in enumerate(sample_lists):
        try:
            last_item = get_last_item(lst)
            print(f"Sample list {i+1}: {lst}")
            print(f"The last item in sample list {i+1} is: {last_item}\n")
        except ValueError as e:
            print(f"Sample list {i+1}: {lst}")
            print(e, "\n")