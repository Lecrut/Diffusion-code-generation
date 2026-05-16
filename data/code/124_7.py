def analyze_numbers(a, b, c):
    numbers = [a, b, c]
    largest = max(numbers)
    smallest = min(numbers)
    mean = (a + b + c) / 3
    return largest, smallest, mean
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    num3 = 15
    largest_num, smallest_num, mean_num = analyze_numbers(num1, num2, num3)
    print(f"The numbers are: {num1}, {num2}, {num3}")
    print(f"The largest number is: {largest_num}")
    print(f"The smallest number is: {smallest_num}")
    print(f"The arithmetic mean is: {mean_num}")