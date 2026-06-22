def calculate_averages(data):
    if not data:
        return []
    
    first_elements = [item[0] for item in data]
    second_elements = [item[1] for item in data]
    
    avg_first = sum(first_elements) / len(first_elements) if first_elements else 0.0
    avg_second = sum(second_elements) / len(second_elements) if second_elements else 0.0
    
    return [avg_first, avg_second]

if __name__ == '__main__':
    sample_data = [(10, 20), (30, 40), (50, 60), (70, 80)]
    averages = calculate_averages(sample_data)
    print(f"{averages=}")