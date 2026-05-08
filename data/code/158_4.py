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