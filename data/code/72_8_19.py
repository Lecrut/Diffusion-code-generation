def compare_elements(data_list, indices):
    for i, j in zip(indices, indices[1:]):
        if data_list[i] < data_list[j]:
            print(f"{data_list[i]} is less than {data_list[j]}")
        elif data_list[i] > data_list[j]:
            print(f"{data_list[i]} is greater than {data_list[j]}")
        else:
            print(f"{data_list[i]} is equal to {data_list[j]}")

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    sample_indices = [0, 2, 4]
    compare_elements(sample_data, sample_indices)