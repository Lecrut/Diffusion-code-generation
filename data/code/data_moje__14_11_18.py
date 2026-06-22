def get_third_item(arr):
    try:
        return arr[2]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_third_item(sample_list)
    print(result)