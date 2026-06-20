def access_list_elements(data, indices):
    return [data[index] for index in indices if 0 <= index < len(data)]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    sample_indices = [0, 2, 4, 6]
    print(access_list_elements(sample_data, sample_indices))