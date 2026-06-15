def process_set(integer_set):
    even_numbers = []
    for number in integer_set:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
if __name__ == '__main__':
    sample_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    result = process_set(sample_set)
    print(result)