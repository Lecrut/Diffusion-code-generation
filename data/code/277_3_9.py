def count_even_numbers(numbers):
    count = 0
    index = 0
    while index < len(numbers):
        if numbers[index] % 2 == 0:
            count += 1
        index += 1
    return count

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = count_even_numbers(sample_list)
    print(f"Number of even numbers in {sample_list}: {result}")