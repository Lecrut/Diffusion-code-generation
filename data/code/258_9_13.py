def calculate_averages(data):
    if not data:
        return [0.0]
    
    total = 0.0
    count = len(data)
    
    for number in data:
        total += number
    
    avg = total / count
    return [avg]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = calculate_averages(sample_data)
    print(f"{result=}")