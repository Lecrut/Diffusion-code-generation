def compute_total(values):
    return sum(values)

if __name__ == '__main__':
    sample_values = [1, 3, 5, -2, 4]
    total_result = compute_total(sample_values)
    print(total_result)
    empty_list = []
    total_empty = compute_total(empty_list)
    print(total_empty)