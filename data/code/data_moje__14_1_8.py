def get_third_item(arr):
    try:
        return arr[2]
    except IndexError:
        return None

if __name__ == '__main__':
    predefined_array = [10, 20, 30, 40, 50]
    result = get_third_item(predefined_array)
    print(result)