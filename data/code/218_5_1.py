import sys
if __name__ == '__main__':
    data = [10, 5, 20, 3, 15]
    minimum = data[0]
    for number in data:
        if number < minimum:
            minimum = number
    print(minimum)