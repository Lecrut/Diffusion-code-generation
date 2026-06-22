def get_middle_item(array):
    return array[len(array) // 2]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = get_middle_item(sample_data)
    print(result)