import sys
if __name__ == '__main__':
    input_data = "5,1,8,3,9,2"
    numbers = [int(x.strip()) for x in input_data.split(',')]
    sorted_numbers = sorted(numbers)
    print(*(sorted_numbers))