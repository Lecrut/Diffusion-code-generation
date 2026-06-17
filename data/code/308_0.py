def count_elements(data):
    count = 0
    for element in data:
        count += 1
    return count
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    result = count_elements(sample_list)
    print(result)