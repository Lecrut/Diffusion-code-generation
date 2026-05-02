def find_final_index(data, target):
    last_index = -1
    for i in range(len(data)):
        if data[i] == target:
            last_index = i
    return last_index
if __name__ == '__main__':
    sample_list = [10, 20, 30, 20, 40, 20]
    target_value = 20
    final_index = find_final_index(sample_list, target_value)
    print(final_index)