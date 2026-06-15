import sys
if __name__ == '__main__':
    data = [10, 5, 20, 15, 30, 8]
    max_value = -sys.maxsize - 1
    for num in data:
        if num > max_value:
            max_value = num
    print(max_value)