def calculate_average(data):
    if not data:
        return 0
    total = 0
    for x in data:
        total += x
    return total / len(data)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    average = calculate_average(sample_list)
    print(average)