def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    print(average([1, 2, 3, 4, 5]))
    print(average([7]))