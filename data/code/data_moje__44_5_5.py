def _is_valid_scores_list(data):
    if not isinstance(data, list):
        return False
    for item in data:
        if not isinstance(item, (int, float)):
            return False
    return True

def _calculate_total(values):
    current_sum = 0
    for value in values:
        current_sum += value
    return current_sum

def _get_count(values):
    return len(values)

def compute_test_score_average(scores):
    if not _is_valid_scores_list(scores):
        raise TypeError("Input must be a list of numbers")
    count = _get_count(scores)
    if count == 0:
        return 0.0
    total = _calculate_total(scores)
    return total / count

if __name__ == '__main__':
    sample_data = [85.5, 90.0, 78.5, 92.0, 88.0, 75.5]
    average_value = compute_test_score_average(sample_data)
    print(average_value)