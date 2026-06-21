def sort_and_count(numbers):
    even_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
    sorted_numbers = sorted(numbers)
    return sorted_numbers, even_count

if __name__ == '__main__':
    sample_values = [5, 3, 8, 6, 2, 7, 4, 1]
    result = sort_and_count(sample_values)
    print(result)