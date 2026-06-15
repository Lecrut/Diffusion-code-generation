import sys
if __name__ == '__main__':
    input_line = "10 5 20 8 15"
    numbers = input_line.split()
    if numbers:
        integer_list = [int(x) for x in numbers]
        maximum_value = max(integer_list)
        print(maximum_value)