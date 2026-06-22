import operator

def calculate_area(base, height):
    return operator.mul(base, height)

if __name__ == '__main__':
    base_value = 10
    height_value = 5
    result = calculate_area(base_value, height_value)
    print(result)