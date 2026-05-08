def calculate_list_sum(data_list):
    total = 0
    for item in data_list:
        total += item
    return total
if __name__ == '__main__':
    sample_list = [10, 5.5, -3, 12.25, 0]
    result = calculate_list_sum(sample_list)
    print(result)