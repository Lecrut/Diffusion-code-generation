EVEN_NUMBER_THRESHOLD = 2

def count_even_numbers(numbers):
    even_count = 0
    index = 0
    while index < len(numbers):
        if numbers[index] % EVEN_NUMBER_THRESHOLD == 0:
            even_count += 1
        index += 1
    return even_count

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6]
    result = count_even_numbers(sample_list)
    print(f"Number of even numbers in {sample_list}: {result}")