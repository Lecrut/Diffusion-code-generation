def count_even_numbers(numbers):
    return sum(1 for number in numbers if number % 2 == 0)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6]
    print(count_even_numbers(sample_values))