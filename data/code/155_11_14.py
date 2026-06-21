def calculate_sum(data):
    total = 0
    for number in data:
        total += number
    return total

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    result = calculate_sum(sample_values)
    print(result)