def calculate_mean(data):
    total = sum(data)
    count = len(data)
    return total / count

if __name__ == '__main__':
    sample_numbers = [2.5, 3.9, 4.1, 5.6]
    mean_value = calculate_mean(sample_numbers)
    print(mean_value)