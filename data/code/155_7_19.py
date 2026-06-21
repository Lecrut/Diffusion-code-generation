def calculate_sum(numbers):
    total = 0
    for number in numbers:
        if isinstance(number, (int, float)):
            total += number
    return total

if __name__ == '__main__':
    sample_list = [1.5, 2, 3.5, 4]
    result = calculate_sum(sample_list)
    print(result)