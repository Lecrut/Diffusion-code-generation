def get_third_item(array):
    if len(array) >= 3:
        return array[2]
    return None

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = get_third_item(sample_data)
    print(result)