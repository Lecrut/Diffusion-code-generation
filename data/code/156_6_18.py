def calculate_average(data):
    if not data:
        return 0
    total = sum(data)
    count = len(data)
    return total / count

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    average = calculate_average(sample_list)
    print(average)