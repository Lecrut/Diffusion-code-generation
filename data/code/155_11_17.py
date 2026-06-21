def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = calculate_sum(sample_list)
    print(result)