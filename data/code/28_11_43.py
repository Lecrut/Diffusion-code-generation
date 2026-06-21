def is_larger(num1, num2):
    return num1 > num2

if __name__ == '__main__':
    sample_values = [
        (10, 5),
        (3, 7),
        (-1, -2),
        (0, 0),
        (5.5, 2)
    ]
    
    for val1, val2 in sample_values:
        print(is_larger(val1, val2))