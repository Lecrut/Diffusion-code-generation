def filter_odd_numbers(data):
    odd_nums = []
    for item in data:
        if item % 2 != 0:
            odd_nums.append(item)
    return odd_nums
if __name__ == '__main__':
    sample_data = [10, 23, 45, 68, 91]
    result = filter_odd_numbers(sample_data)
    print(result)