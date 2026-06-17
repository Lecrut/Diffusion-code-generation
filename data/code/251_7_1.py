import sys
if __name__ == '__main__':
    data = [10, 5, 20, 3, 15]
    max_val = -sys.maxsize - 1
    for num in data:
        if num > max_val:
            max_val = num
    print(max_val)