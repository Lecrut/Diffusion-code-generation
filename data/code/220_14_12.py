def calculate_total_and_count(data):
    if not data:
        return 0, 0
    total_sum = sum(sum(s) for s in data)
    total_count = sum(len(s) for s in data)
    return total_sum, total_count

def compute_average_of_sets(list_of_sets):
    total_sum, total_count = calculate_total_and_count(list_of_sets)
    if total_count == 0:
        return 0
    return total_sum / total_count

if __name__ == '__main__':
    sample_data = [
        {1, 2, 3},
        {4, 5},
        {6, 7, 8, 9}
    ]
    result = compute_average_of_sets(sample_data)
    print(result)