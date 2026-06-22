def average(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    return total / count

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = average(sample_list)
    print(result)