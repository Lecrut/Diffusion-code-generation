def calculate_averages(data):
    if not data:
        return [0.0]
    
    total_sum = 0.0
    count = 0
    
    for item in data:
        total_sum += float(item)
        count += 1
    
    average = total_sum / count
    return [average]

if __name__ == '__main__':
    sample_data = ['1', '2', '3', '4']
    averages = calculate_averages(sample_data)
    print(f"{averages=}")