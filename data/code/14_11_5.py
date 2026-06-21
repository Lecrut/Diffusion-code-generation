def get_third_item(arr):
    if len(arr) >= 3:
        return arr[2]
    return None

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_third_item(sample_list)
    print(result)