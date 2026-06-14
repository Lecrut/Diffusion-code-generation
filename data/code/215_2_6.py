import sys
if __name__ == '__main__':
    input_line = "10 5 22 8 30"
    numbers = input_line.split()
    integer_list = [int(x) for x in numbers]
    maximum_value = max(integer_list)
    print(maximum_value)