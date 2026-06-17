def swap_neighbors(data_list):
    if len(data_list) < 2:
        return data_list
    n = len(data_list) - 1
    temp = data_list[n]
    data_list[n] = data_list[n-1]
    data_list[n-1] = temp
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    swap_neighbors(sample_data)
    print(f"Original: {sample_data}")