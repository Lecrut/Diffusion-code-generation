def calculate_total(numbers):
    return sum(numbers) if numbers else 0

if __name__ == '__main__':
    sample_list = [5, 15, 25]
    total_sum = calculate_total(sample_list)
    print(total_sum)