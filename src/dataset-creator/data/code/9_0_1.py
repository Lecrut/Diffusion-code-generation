if __name__ == '__main__':
    numbers = [10, 25, 32, 18, 45]
    if not numbers:
        mean = 0
    else:
        mean = sum(numbers) / len(numbers)
    print(mean)