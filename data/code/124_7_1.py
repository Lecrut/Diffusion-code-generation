def analyze_numbers(num1, num2, num3):
    numbers = [num1, num2, num3]
    largest = max(numbers)
    smallest = min(numbers)
    mean = (num1 + num2 + num3) / 3
    return largest, smallest, mean
if __name__ == '__main__':
    a = 10
    b = 5
    c = 15
    largest_num, smallest_num, mean_num = analyze_numbers(a, b, c)
    print(f"Largest number: {largest_num}")
    print(f"Smallest number: {smallest_num}")
    print(f"Arithmetic mean: {mean_num}")