def are_close(num1, num2, tolerance=1e-9):
    return abs(num1 - num2) <= tolerance

if __name__ == '__main__':
    print(are_close(0.1 + 0.2, 0.3))