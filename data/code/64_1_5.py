def find_final_index(data_list, target_item):
    try:
        return data_list[::-1].index(target_item)
    except ValueError:
        return -1

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 2, 5, 2]
    target = 2
    result = find_final_index(sample_data, target)
    print(result)