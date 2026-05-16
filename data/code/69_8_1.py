def get_sublist(data, start, end):
    return data[start:end+1]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60, 70]
    start_index = 2
    end_index = 5
    sublist = get_sublist(sample_list, start_index, end_index)
    print(sublist)