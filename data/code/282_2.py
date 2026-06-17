def sum_even_numbers(data):
    total = 0
    for number in data:
        if number % 2 == 0:
            total += number
    return total
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = sum_even_numbers(sample_list)
    print(result)