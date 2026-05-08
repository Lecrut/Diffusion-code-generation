def analyze_conditions(data):
    total_sum = 0
    for condition, value in data:
        if condition:
            total_sum += value
    return total_sum
if __name__ == '__main__':
    sample_data = [
        (True, 10),
        (False, 20),
        (True, 30),
        (False, 40),
        (True, 50)
    ]
    result = analyze_conditions(sample_data)
    print(result)