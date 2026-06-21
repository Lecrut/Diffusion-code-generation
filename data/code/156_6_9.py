def calculate_average(data):
    if not data:
        return 0
    total = sum(data)
    count = len(data)
    return total / count

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    average = calculate_average(sample_list)
    print(average)