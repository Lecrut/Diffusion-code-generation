def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    maximum = data[0]
    for number in data[1:]:
        if number > maximum:
            maximum = number
    return maximum

if __name__ == '__main__':
    sample_lists = {
        "sample_list1": [3, 1, 4, 1, 5, 9, 2],
        "sample_list2": [-10, -5, -20, -1],
        "sample_list3": [42],
        "sample_list4": [100, 50, 25]
    }
    
    for key, sample_list in sample_lists.items():
        print(f"The maximum of {key}: {find_maximum(sample_list)}")