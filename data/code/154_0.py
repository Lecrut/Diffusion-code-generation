def count_elements(data):
    count = 0
    for element in data:
        count += 1
    return count
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = count_elements(sample_list)
    print(result)