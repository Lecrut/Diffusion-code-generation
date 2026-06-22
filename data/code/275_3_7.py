def count_even_numbers(numbers):
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements in the list must be integers")
    return sum(1 for num in numbers if num % 2 == 0)

if __name__ == '__main__':
    data = [10, 25, 15, 30]
    result = count_even_numbers(data)
    print(result)