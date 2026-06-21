def calculate_average(numbers):
    total = sum(x for x in numbers)
    count = len(numbers)
    average = total / count if count > 0 else 0
    return average

if __name__ == '__main__':
    sample = [45, 55, 65]
    avg = calculate_average(sample)
    print(avg)