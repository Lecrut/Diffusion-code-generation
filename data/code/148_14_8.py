from functools import reduce

def find_largest_element(data):
    return reduce(lambda x, y: x if x > y else y, data)

if __name__ == '__main__':
    sample_lists = {
        "List 1": [10, 5, 20, 8, 15],
        "List 2": [-5, -1, -10, -2],
        "List 3": [7, 7, 7, 7],
        "List 4": [42],
        "List 5": [-100, 0, -50]
    }
    
    for name, sample_list in sample_lists.items():
        print(f"{name}: {sample_list}, Largest element: {find_largest_element(sample_list)}")