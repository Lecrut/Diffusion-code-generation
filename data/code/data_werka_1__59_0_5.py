def find_middle_item(data):
    n = len(data)
    middle_index = (n - 1) // 2
    return data[middle_index]

if __name__ == '__main__':
    sample_lists = {
        'odd_length': [1, 2, 3, 4, 5],
        'even_length': [10, 20, 30, 40],
        'single_element': [100],
        'another_odd': [5, 15, 25, 35, 45, 55]
    }
    
    for key, value in sample_lists.items():
        print(f"Middle item of {key} list: {find_middle_item(value)}")