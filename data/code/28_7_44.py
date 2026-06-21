def is_larger(a, b):
    return a > b

if __name__ == '__main__':
    sample_values = [
        (10, 5),
        (3, 7),
        (-1, -2),
        (0, 0),
        (1.5, 1.4),
        (2, 2.0),
        (1e6, 999999)
    ]
    
    for a, b in sample_values:
        print(is_larger(a, b))