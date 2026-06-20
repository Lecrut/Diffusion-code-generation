def calculate_average(values):
    if not values:
        return 0
    total = sum(values)
    count = len(values)
    average = total / count
    return average

if __name__ == '__main__':
    sample_list = [25, 35, 45, 55]
    avg = calculate_average(sample_list)
    print(avg)