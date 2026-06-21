def compute_total(numbers):
    return sum(numbers)

if __name__ == '__main__':
    sample_values = [15, 20, -5, 30, 10]
    total_sum = compute_total(sample_values)
    print(total_sum)
    empty_list = []
    result_empty = compute_total(empty_list)
    print(result_empty)