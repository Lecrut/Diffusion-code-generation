def calculate_range(data):
    try:
        numbers = [float(x) for x in data if str(x).replace('.', '', 1).isdigit()]
        if not numbers:
            return None
        min_val = min(numbers)
        max_val = max(numbers)
        return max_val - min_val
    except ValueError:
        return None

if __name__ == '__main__':
    sample_data = ['3.14159', '1.61803', '2.71828', '0.57721', '4.0', 'a', '1.0']
    range_result = calculate_range(sample_data)
    print(range_result)