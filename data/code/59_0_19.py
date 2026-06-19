def find_middle_item(data):
    n = len(data)
    middle_index = (n - 1) // 2
    return data[middle_index]

if __name__ == '__main__':
    sample_lists = {
        'odd': [1, 3, 5, 7, 9],
        'even': [10, 20, 30, 40],
        'single': [42],
        'more_even': [1, 2, 3, 4, 5, 6]
    }
    
    for key, lst in sample_lists.items():
        print(f"Middle item of {key} list: {find_middle_item(lst)}")