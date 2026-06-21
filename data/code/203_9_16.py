TOLERANCE = 1e-9

def are_close(num1, num2):
    return abs(num1 - num2) <= TOLERANCE

if __name__ == '__main__':
    print(are_close(0.1 + 0.2, 0.3))