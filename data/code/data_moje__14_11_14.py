def get_third_item(arr):
    if len(arr) >= 3:
        return arr[2]
    return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_third_item(sample_list))