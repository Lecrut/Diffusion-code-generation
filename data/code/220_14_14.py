def calculate_mean(data):
    if not data:
        raise ValueError('Input list cannot be empty')
    total_sum = sum(data)
    count = len(data)
    if count == 0:
        return 0
    return total_sum / count
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    try:
        result = calculate_mean(sample_data)
        print(result)
    except ValueError as e:
        print(e)