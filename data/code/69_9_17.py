def access_list_elements(data, indices):
    result = []
    for index in indices:
        try:
            element = data[index]
            result.append(element)
        except IndexError:
            print(f'Index {index} is out of bounds. Skipping.')
    return result
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    sample_indices = [0, 2, 4, 6]
    print(access_list_elements(sample_data, sample_indices))