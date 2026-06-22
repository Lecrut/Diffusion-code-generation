import operator

def calculate_area(base, height):
    return operator.mul(base, height)

if __name__ == '__main__':
    result = calculate_area(10, 5)
    print(result)