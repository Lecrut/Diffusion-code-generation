def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = (10, 20, 30, 40, 50)
    print(average(sample_values))