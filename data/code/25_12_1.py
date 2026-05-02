import sys
if __name__ == '__main__':
    input_data = [1, 0, 5, 0, -3, 0, 10]
    result = ["zero" if x == 0 else "not zero" for x in input_data]
    print(*result)