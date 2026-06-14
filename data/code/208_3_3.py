if __name__ == '__main__':
    input_data = [10, 20, 30, 40, 50]
    numbers = input_data
    if not numbers:
        mean = 0
    else:
        total = sum(numbers)
        count = len(numbers)
        mean = total / count
    print(f"The sequence of numbers is: {numbers}")
    print(f"The mean is: {mean}")