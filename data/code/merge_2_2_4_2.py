def is_positive(x):
    return x > 0
if __name__ == '__main__':
    test_values = [-5, -1, 0, 1, 3.14]
    for val in test_values:
        print(f"{val}: {is_positive(val)}")