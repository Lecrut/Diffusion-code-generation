def are_values_equal(a, b):
    return a == b
if __name__ == '__main__':
    print(f"10 == 10: {are_values_equal(10, 10)}")
    print(f"'hello' == 'hello': {are_values_equal('hello', 'hello')}")
    print(f"3.14 == 3.14: {are_values_equal(3.14, 3.14)}")
    print(f"5 == 6: {are_values_equal(5, 6)}")
    print(f"True == True: {are_values_equal(True, True)}")
    print(f"False == 0: {are_values_equal(False, 0)}")
    print(f"1 == '1': {are_values_equal(1, '1')}")