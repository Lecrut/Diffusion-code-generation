import timeit
def find_optimal_entry(data_list):
    if not data_list:
        return None
    max_val = float('-inf')
    optimal_index = 0
    for i, val in enumerate(data_list):
        current_metric = (val ** 2) + abs(val - data_list[i-1] if i > 0 else 0)
        if current_metric > max_val:
            max_val = current_metric
            optimal_index = i
    return data_list[optimal_index]
if __name__ == '__main__':
    sample_data = [1, 3, -2, 5, 7, 4, 9, 0, 8, 6] * 100
    start_time = timeit.default_timer()
    result_entry = find_optimal_entry(sample_data)
    end_time = timeit.default_timer()
    print(f"Optimal initial list entry: {result_entry}")