def sort_and_count(numbers):
    sorted_numbers = sorted(numbers)
    even_count = sum(1 for num in numbers if num % 2 == 0)
    return sorted_numbers, even_count

if __name__ == '__main__':
    sample_list = [5, 3, 6, 2, 8, 1, 4]
    result = sort_and_count(sample_list)
    print(result)