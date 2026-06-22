def count_even_numbers(numbers):
    even_count = 0
    for number in numbers:
        if number % 2 == 0:
            even_count += 1
    return even_count

if __name__ == '__main__':
    sample_data = [4, 7, 8, 13, 16, 19]
    result = count_even_numbers(sample_data)
    print(result)