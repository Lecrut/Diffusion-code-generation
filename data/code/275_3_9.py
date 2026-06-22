def count_even_numbers(numbers):
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements in the list must be integers.")
    
    even_count = 0
    for number in numbers:
        if number % 2 == 0:
            even_count += 1
    
    return even_count

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6]
    result = count_even_numbers(sample_values)
    print(result)