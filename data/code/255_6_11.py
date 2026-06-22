def find_max_element(data):
    max_elem = data[0]
    for elem in data:
        if elem > max_elem:
            max_elem = elem
    return max_elem

if __name__ == '__main__':
    sample_data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    print(find_max_element(sample_data))