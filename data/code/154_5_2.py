def count_occurrences(data_list):
    count = 0
    for item in data_list:
        count += 1
    return count
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 1, 5, 1, 6, 1]
    result = count_occurrences(sample_list)
    print(result)