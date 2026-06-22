def compare_two_simple_quantities_now_summary():
    sample_values = [3, 5, 2, 8, 4]
    summary_stats = {
        'mean': sum(sample_values) / len(sample_values),
        'min': min(sample_values),
        'max': max(sample_values)
    }
    return summary_stats

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_summary()
    print(result)