def calculate_sum(values):
    return sum(filter(lambda x: isinstance(x, (int, float)), values))
if __name__ == '__main__':
    sample_values = [10, 25, 'hello', 30, -5, 30.5]
    result = calculate_sum(sample_values)
    print(result)