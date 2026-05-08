def calculate_mixed_sum(data):
    total = 0
    for item in data:
        try:
            total += float(item)
        except (ValueError, TypeError):
            pass
    return total
if __name__ == '__main__':
    sample_list = [10, 5.5, "20", "error", 3.14, None, [1, 2]]
    result = calculate_mixed_sum(sample_list)
    print(result)