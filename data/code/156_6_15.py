def calculate_average(data):
    if not data:
        return 0
    total = sum(data)
    count = len(data)
    average = total / count
    return average

if __name__ == '__main__':
    sample_list = [12, 34, 56, 78]
    average = calculate_average(sample_list)
    print(average)