def calculate_mean(data):
    if not data:
        return 0.0
    total = sum(data)
    count = len(data)
    average = total / count
    return average

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5]
    result = calculate_mean(sample_values)
    print(f"Average of {sample_values}: {result}")