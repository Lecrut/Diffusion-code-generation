def find_middle_index(arr):
    if not arr:
        return -1
    length = len(arr)
    return length // 2
if __name__ == '__main__':
    sample_array = [10, 20, 30, 40, 50]
    index = find_middle_index(sample_array)
    print(index)