def compare_two_simple_quantities_now_summary():
    sample_values = [10, 20, 30, 40, 50]
    summary_stats = {
        'mean': sum(sample_values) / len(sample_values),
        'max': max(sample_values),
        'min': min(sample_values)
    }
    return summary_stats

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_summary()
    print(result)