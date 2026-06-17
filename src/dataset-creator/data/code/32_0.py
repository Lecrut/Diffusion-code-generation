def count_unique_elements(data_list):
    return len(set(data_list))
if __name__ == '__main__':
    sample_list = [1, 2, 2, 3, 4, 4, 4, 5, 1]
    unique_count = count_unique_elements(sample_list)
    print(unique_count)