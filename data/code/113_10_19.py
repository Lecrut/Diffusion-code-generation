MIN_DIFFERENCE = 0

def calculate_difference(a, b):
    return max(a - b, MIN_DIFFERENCE)
if __name__ == '__main__':
    result = calculate_difference(10, 5)
    print(result)