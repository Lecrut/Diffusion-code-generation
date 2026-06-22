def calculate_cumulative_sum(data):
    return tuple((sum(data[:i + 1]) for i in range(len(data))))
if __name__ == '__main__':
    sample_values = (10, 20, 30, 40, 50)
    result = calculate_cumulative_sum(sample_values)
    print(result)