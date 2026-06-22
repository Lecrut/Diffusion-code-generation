def count_even_numbers(numbers):
    return sum(1 for num in numbers if num % 2 == 0)

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6]
    result = count_even_numbers(data)
    print(result)