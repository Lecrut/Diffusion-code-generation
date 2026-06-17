def count_items(data):
    count = 0
    for item in data:
        count += 1
    return count
if __name__ == '__main__':
    sample_list = [1, 5, 10, 15, 20]
    result = count_items(sample_list)
    print(result)