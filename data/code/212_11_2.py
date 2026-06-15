def calculate_range(data):
    if not data:
        return 0
    return max(data) - min(data)
if __name__ == '__main__':
    sample_list = [10, 5, 20, 3, 15]
    result = calculate_range(sample_list)
    print(result)