def filter_odd_numbers(sequence):
    odd_numbers = []
    for number in sequence:
        if number % 2 != 0:
            odd_numbers.append(number)
    return odd_numbers
if __name__ == '__main__':
    input_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_odd_numbers(input_sequence)
    print(result)