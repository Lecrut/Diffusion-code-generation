def compute_total(values):
    return sum(values)

if __name__ == '__main__':
    sample_values = [1, 3, 5, -2, 7]
    total_result = compute_total(sample_values)
    print(total_result)
    empty_list = []
    result_empty = compute_total(empty_list)
    print(result_empty)