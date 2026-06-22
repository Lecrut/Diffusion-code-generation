def find_middle(data):
    if not data:
        raise ValueError("The list is empty")
    middle_index = len(data) // 2
    return data[middle_index]

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        [99],
        [5, 10, 15, 20]
    ]
    for lst in sample_lists:
        print(find_middle(lst))