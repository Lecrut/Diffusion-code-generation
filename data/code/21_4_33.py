def sort_and_count(numbers):
    sorted_numbers = sorted(numbers)
    even_count = sum(1 for num in numbers if num % 2 == 0)
    return sorted_numbers, even_count

if __name__ == '__main__':
    sample_values = [34, 7, 23, 32, 5, 62]
    result = sort_and_count(sample_values)
    print(result)