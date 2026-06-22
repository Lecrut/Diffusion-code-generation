def average_of_list(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = average_of_list(sample_data)
    print(result)