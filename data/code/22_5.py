import sys
if __name__ == '__main__':
    input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for num in input_data:
        if num % 2 == 0:
            print('Even')
        else:
            print('Odd')