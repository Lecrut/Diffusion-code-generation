def find_odd_numbers(data):
    odd_numbers = []
    for number in data:
        if number % 2 != 0:
            odd_numbers.append(number)
    return odd_numbers
if __name__ == '__main__':
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = find_odd_numbers(input_list)
    print(result)