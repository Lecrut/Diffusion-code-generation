def count_items(data):
    count = 0
    index = 0
    while index < len(data):
        count += 1
        index += 1
    return count
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    result = count_items(sample_list)
    print(result)