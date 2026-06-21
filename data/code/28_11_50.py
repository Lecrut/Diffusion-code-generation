def is_larger(num1, num2):
    return num1 > num2

if __name__ == '__main__':
    SAMPLE_VALUES = [
        (10, 5),
        (3, 7),
        (-1, -5),
        (0, 0),
        (5.5, 2),
        (100, 100),
        (-10, -20),
        (0.1, 0.2)
    ]
    
    for num1, num2 in SAMPLE_VALUES:
        print(is_larger(num1, num2))