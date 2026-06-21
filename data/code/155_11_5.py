sample_data = {10: 20, 30: 40, 50: 60}

def calculate_sum(data):
    return sum(data.values())

if __name__ == '__main__':
    result = calculate_sum(sample_data)
    print(result)