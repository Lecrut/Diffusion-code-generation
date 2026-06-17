def find_middle_index(arr):
    if not arr:
        return -1
    length = len(arr)
    mid_index = length // 2
    return mid_index
if __name__ == '__main__':
    sample_array = [10, 20, 30, 40, 50]
    result_index = find_middle_index(sample_array)
    print(result_index)