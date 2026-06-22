def compare_two_simple_quantities_now_summary():
    sample_values = [5, 3, 8, 2, 9]
    summary_stats = {
        'mean': sum(sample_values) / len(sample_values),
        'min': min(sample_values),
        'max': max(sample_values)
    }
    return summary_stats

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_summary()
    print(result)