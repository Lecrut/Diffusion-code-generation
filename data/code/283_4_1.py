def filter_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if isinstance(num, int):
            if num % 2 == 0:
                even_numbers.append(num)
    return even_numbers
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, "a", 9.5]
    result = filter_even_numbers(sample_list)
    print(result)