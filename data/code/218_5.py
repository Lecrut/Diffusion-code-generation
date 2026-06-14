import sys
if __name__ == '__main__':
    data = [15, 3, 8, 22, 1]
    minimum = data[0]
    for number in data:
        if number < minimum:
            minimum = number
    print(minimum)