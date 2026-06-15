def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
if __name__ == '__main__':
    sample_list = [1, 5, 10, 15, 20]
    result = calculate_sum(sample_list)
    print(result)