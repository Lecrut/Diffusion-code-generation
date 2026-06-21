def calculate_average(data):
    if not data:
        return 0
    total_sum = sum(data)
    count = len(data)
    average = total_sum / count
    return average

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45]
    avg = calculate_average(sample_data)
    print(avg)