def extract_middle_item(arr):
    mid_index = len(arr) // 2
    return arr[mid_index]

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    result = extract_middle_item(sample_data)
    print(result)