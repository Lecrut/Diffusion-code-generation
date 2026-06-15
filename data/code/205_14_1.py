import sys
if __name__ == '__main__':
    input_data = "5,1,8,3,2"
    numbers = [int(x.strip()) for x in input_data.split(',')]
    numbers.sort()
    print(*(numbers))