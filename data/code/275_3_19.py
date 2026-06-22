def count_even_numbers(numbers):
    even_count = 0
    for number in numbers:
        if number % 2 == 0:
            even_count += 1
    return even_count

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6]
    result = count_even_numbers(sample_numbers)
    print(result)