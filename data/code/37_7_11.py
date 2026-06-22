import operator

def calculate_area(base, height):
    return operator.mul(base, height)

if __name__ == '__main__':
    print(calculate_area(5, 10))