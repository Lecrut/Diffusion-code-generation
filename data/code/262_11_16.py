def find_min_max(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return (min(data), max(data))

if __name__ == '__main__':
    sample_lists = {
        "list1": [3, 1, 4, 1, 5, 9, 2, 6],
        "list2": [-10, 0, 5, -20, 100]
    }
    
    for key, value in sample_lists.items():
        result = find_min_max(value)
        print(f"List: {value}, Min: {result[0]}, Max: {result[1]}")