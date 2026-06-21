def get_even_numbers(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

if __name__ == '__main__':
    sample_input = [15, 22, 37, 48, 55, 60, 73, 84, 91, 100]
    result = get_even_numbers(sample_input)
    print(result)