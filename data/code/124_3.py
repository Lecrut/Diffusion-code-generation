def calculate_stats(numbers):
    total_sum = sum(numbers)
    product = 1
    for x in numbers:
        product *= x
    average = total_sum / len(numbers) if numbers else 0
    return total_sum, product, average
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    total, prod, avg = calculate_stats(sample_list)
    print(f"Sum: {total}")
    print(f"Product: {prod}")
    print(f"Average: {avg}")