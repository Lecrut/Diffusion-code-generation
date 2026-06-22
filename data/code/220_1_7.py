def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count > 0 else 0
    return average

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(calculate_average(sample_list))