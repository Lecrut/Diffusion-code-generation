def analyze_conditions(data):
    total_sum = 0
    for condition, value in data:
        if condition:
            total_sum += value
    return total_sum
if __name__ == '__main__':
    sample_data = [
        (True, 10),
        (False, 5),
        (True, 20),
        (False, 15),
        (True, 30),
        (False, 25)
    ]
    result = analyze_conditions(sample_data)
    print(result)