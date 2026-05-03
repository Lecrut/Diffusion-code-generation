import sys
if __name__ == '__main__':
    input_data = [1, 0, 5, 0, -3, 0, 10]
    zero_check = [1 if x == 0 else 0 for x in input_data]
    print(zero_check)