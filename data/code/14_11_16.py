def get_third_item(arr):
    try:
        return arr[2]
    except (IndexError, TypeError):
        return None

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_third_item(sample_list)
    print(result)