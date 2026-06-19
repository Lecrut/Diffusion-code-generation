def find_middle_item(data):
    if not isinstance(data, list) or len(data) == 0:
        raise ValueError("Input must be a non-empty list.")
    
    n = len(data)
    middle_index = (n - 1) // 2
    return data[middle_index]

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        [100],
        [5, 15, 25, 35, 45, 55],
        [7, 8, 9, 10]
    ]
    
    for lst in sample_lists:
        print(find_middle_item(lst))