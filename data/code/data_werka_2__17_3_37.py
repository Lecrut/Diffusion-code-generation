def get_even_numbers(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

if __name__ == '__main__':
    sample_data = [15, 28, 37, 46, 55, 64, 73, 82, 91, 100]
    result = get_even_numbers(sample_data)
    print(result)