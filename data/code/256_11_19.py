def calculate_range(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    print(calculate_range([10, 20, 30]))
    print(calculate_range([-5, -10, -15]))
    print(calculate_range([1.5, 2.5, 3.5]))