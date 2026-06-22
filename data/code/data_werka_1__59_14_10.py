def find_middle(data):
    middle_index = len(data) // 2
    return data[middle_index]

if __name__ == '__main__':
    sample_lists = {
        'list1': [1, 2, 3, 4, 5],
        'list2': [10, 20, 30, 40],
        'list3': [99],
        'list4': [100, 200]
    }
    
    for name, lst in sample_lists.items():
        print(f"Middle of {name}: {find_middle(lst)}")