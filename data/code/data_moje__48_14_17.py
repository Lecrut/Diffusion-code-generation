import math

def find_max_element():
    data = [3.14, 2.71, 1.41, 0.57, 9.81, 6.28, 1.73, 2.41, 5.32, 8.04]
    maximum = -math.inf
    for num in data:
        if num > maximum:
            maximum = num
    return maximum

if __name__ == '__main__':
    result = find_max_element()
    print(result)