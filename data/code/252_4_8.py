def compare_two_simple_quantities_now_summary():
    values = [3, 5, 2, 8, 6]
    summary = {
        'mean': sum(values) / len(values),
        'min': min(values),
        'max': max(values)
    }
    return summary

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_summary()
    print(result)