def find_larger_adjacent_elements(data):
    larger_elements = []
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            larger_elements.append(data[i])
        else:
            larger_elements.append(data[i + 1])
    return larger_elements

if __name__ == '__main__':
    sample_list = [5, 3, 8, 2, 9, 1, 7]
    result = find_larger_adjacent_elements(sample_list)
    print(result)