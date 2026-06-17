def count_items(data):
    count = 0
    index = 0
    while index < len(data):
        count += 1
        index += 1
    return count
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = count_items(sample_list)
    print(result)
    sample_list_empty = []
    result_empty = count_items(sample_list_empty)
    print(result_empty)
    sample_list_with_negatives = [-10, 20, -5, 30]
    result_negatives = count_items(sample_list_with_negatives)
    print(result_negatives)