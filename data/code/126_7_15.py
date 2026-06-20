def are_values_equal(a, b):
    return a == b

if __name__ == '__main__':
    print(f"1 == 1: {are_values_equal(1, 1)}")
    print(f"5 == 5: {are_values_equal(5, 5)}")
    print(f"1 == 2: {are_values_equal(1, 2)}")
    print(f"10 == 10: {are_values_equal(10, 10)}")
    print(f"3.14 == 3.14: {are_values_equal(3.14, 3.14)}")
    print(f"2 == 3: {are_values_equal(2, 3)}")