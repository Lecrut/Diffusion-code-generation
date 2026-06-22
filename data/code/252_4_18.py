import statistics

def compare_two_simple_quantities_now_summary():
    sample_values = [3, 5, 2, 8, 6]
    mean_value = statistics.mean(sample_values)
    median_value = statistics.median(sample_values)
    mode_value = statistics.mode(sample_values)
    return {
        'mean': mean_value,
        'median': median_value,
        'mode': mode_value
    }

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_summary()
    print(result)