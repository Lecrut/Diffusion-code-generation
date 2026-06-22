def find_maximum(data_list):
    sorted_data = sorted(data_list, reverse=True)
    return sorted_data[0]

if __name__ == '__main__':
    sample_list_1 = [7, 34, 19, 56, 23]
    print(f"List 1: {sample_list_1}")
    max1 = find_maximum(sample_list_1)
    print(f"Maximum of List 1: {max1}")