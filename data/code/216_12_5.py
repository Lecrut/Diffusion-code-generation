def find_median(numbers):
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2

if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    print(find_median(data))