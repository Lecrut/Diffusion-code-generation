def calculate_total_sum(numbers):
    return sum(numbers)
if __name__ == '__main__':
    sample_numbers = [7, 14, 21, 28]
    intermediate_result = calculate_total_sum(sample_numbers)
    total_sum = intermediate_result + 56
    print(total_sum)