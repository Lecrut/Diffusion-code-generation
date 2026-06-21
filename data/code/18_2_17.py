def extract_middle_item(arr):
    if not arr:
        return None
    return arr[len(arr) // 2]

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    print(extract_middle_item(sample_data))