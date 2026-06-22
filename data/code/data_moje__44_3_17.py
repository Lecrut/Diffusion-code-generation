def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = calculate_average(sample_list)
    print(result)