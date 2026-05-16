import sys
if __name__ == '__main__':
    input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = []
    for number in input_data:
        if number % 2 == 0:
            even_numbers.append(number)
    print(*(even_numbers))