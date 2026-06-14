def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    max_val = data[0]
    for i in range(1, len(data)):
        if data[i] > max_val:
            max_val = data[i]
    return max_val
if __name__ == '__main__':
    sample_list1 = [3, 1, 4, 1, 5, 9, 2]
    print(find_maximum(sample_list1))
    sample_list2 = [-10, -5, -20, -1]
    print(find_maximum(sample_list2))
    sample_list3 = [42]
    print(find_maximum(sample_list3))
    sample_list4 = [7]
    print(find_maximum(sample_list4))