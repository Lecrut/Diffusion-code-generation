import sys
if __name__ == '__main__':
    data = [15, 3, 8, 2, 20]
    smallest = data[0]
    for num in data:
        if num < smallest:
            smallest = num
    print(smallest)