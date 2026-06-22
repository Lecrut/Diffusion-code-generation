def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return data[0]

if __name__ == '__main__':
    sample_lists = {
        "list1": [5, 2, 8, 1, 9],
        "list2": [],
        "list3": [-10, -5, -20]
    }
    
    for name, lst in sample_lists.items():
        try:
            result = find_minimum(lst)
            print(f"Minimum of {name}: {result}")
        except ValueError as e:
            print(e)