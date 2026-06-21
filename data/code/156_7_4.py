def average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

if __name__ == '__main__':
    print(average([1, 2, 3, 4, 5]))
    print(average([]))