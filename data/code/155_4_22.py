def sum_numbers(numbers):
    return sum(numbers) if numbers else 0

if __name__ == '__main__':
    print(sum_numbers([1, 2, 3]))
    print(sum_numbers([]))