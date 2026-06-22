def sort_and_count(numbers):
    sorted_list = sorted(numbers)
    even_count = sum(1 for num in numbers if num % 2 == 0)
    return sorted_list, even_count

if __name__ == '__main__':
    sample_values = [5, 3, 8, 6, 2, 7, 4, 1]
    result = sort_and_count(sample_values)
    print(result)