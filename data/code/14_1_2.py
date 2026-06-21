def get_third_item(arr):
    if len(arr) >= 3:
        return arr[2]
    else:
        raise IndexError("Array does not have a third item")

if __name__ == '__main__':
    predefined_array = [10, 20, 30, 40, 50]
    try:
        result = get_third_item(predefined_array)
        print(result)
    except IndexError as e:
        print(str(e))