if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    sentinel = -1
    running_sum = 0
    for number in data:
        running_sum += number
        count = len(data)
        running_average = running_sum / count
        print(f"Input: {number}, Running Average: {running_average}")