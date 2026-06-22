def get_middle_value(array):
    if not array:
        return None
    mid_index = len(array) // 2
    return array[mid_index]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    print(get_middle_value(sample_data))