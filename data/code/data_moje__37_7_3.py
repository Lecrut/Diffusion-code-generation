import operator

def calculate_area(base, height):
    return operator.mul(base, height)

if __name__ == '__main__':
    base = 10
    height = 5
    print(calculate_area(base, height))