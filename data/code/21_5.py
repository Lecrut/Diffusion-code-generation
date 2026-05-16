def sort_and_count(numbers):
    sorted_numbers = sorted(numbers)
    even_count = 0
    for number in numbers:
        if number % 2 == 0:
            even_count += 1
    return (sorted_numbers, even_count)
if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 10, 3, 6, 7]
    result = sort_and_count(sample_list)
    print(result)