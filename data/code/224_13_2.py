def calculate_mean(data):
    total = sum(data)
    count = len(data)
    average = total / count
    return average

if __name__ == '__main__':
    sample_array = [10, 20, 30, 40]
    result = calculate_mean(sample_array)
    print(result)