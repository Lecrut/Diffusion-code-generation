import operator

def calculate_area(base, height):
    return operator.mul(base, height)

if __name__ == '__main__':
    base = 5
    height = 10
    area = calculate_area(base, height)
    print(area)