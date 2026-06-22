def find_max_element(data):
    max_value = data[0]
    for value in data:
        if value > max_value:
            max_value = value
    return max_value

if __name__ == '__main__':
    sample_data = [3, 5, 1, 2, 4, 8, 7, 6]
    print(find_max_element(sample_data))