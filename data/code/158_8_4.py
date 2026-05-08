def find_even_numbers(data):
    even_numbers = []
    for number in data:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = find_even_numbers(sample_list)
    print(result)
    sample_list_2 = [1, 3, 5, 7, 9]
    result_2 = find_even_numbers(sample_list_2)
    print(result_2)
    sample_list_3 = [10, 20, 30, 40]
    result_3 = find_even_numbers(sample_list_3)
    print(result_3)