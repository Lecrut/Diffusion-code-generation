import sys
if __name__ == '__main__':
    input_data = [1, 0, 5, 0, -2, 0, 10]
    zero_check = [1 if x == 0 else 0 for x in input_data]
    for result in zero_check:
        print(result)