def get_middle_item(array):
    if len(array) == 0:
        return None
    index = len(array) // 2
    return array[index]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = get_middle_item(sample_data)
    print(result)