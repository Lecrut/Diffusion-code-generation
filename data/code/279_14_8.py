def cycle_positive_numbers(start=-10, end=10):
    return [num for num in range(start, end + 1) if num > 0]

if __name__ == '__main__':
    positive_numbers = cycle_positive_numbers()
    print("Positive numbers from -10 to 10:", positive_numbers)