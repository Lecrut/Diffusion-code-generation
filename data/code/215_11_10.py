def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for x in data[1:]:
        if x > largest:
            largest = x
    return largest

if __name__ == '__main__':
    sample_lists = {
        'list1': [3, 1, 4, 1, 5, 9, 2],
        'list2': [-10, -5, -20, -1],
        'list3': [42],
        'list4': [100, 50, 200, 10]
    }
    
    for key, value in sample_lists.items():
        print(f"The largest in {value} is: {find_largest(value)}")