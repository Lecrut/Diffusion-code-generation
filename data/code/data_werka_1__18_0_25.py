def is_strictly_greater(a, b):
    try:
        return float(a) > float(b)
    except (ValueError, TypeError):
        return False

if __name__ == '__main__':
    sample_values = [(5, 3), ('10', '2'), (7.5, 8.0), ('abc', 5), (4, 'xyz')]
    results = [is_strictly_greater(a, b) for a, b in sample_values]
    print(results)