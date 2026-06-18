def find_average(numbers):
    total = 0
    count = 0
    for number in numbers:
        total += number
        count += 1
    if count == 0:
        return 0
    return total / count
if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    average = find_average(data)
    print(average)