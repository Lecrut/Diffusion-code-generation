def are_values_equal(a, b):
    return a == b
if __name__ == '__main__':
    print(f"Are 5 and 5 equal? {are_values_equal(5, 5)}")
    print(f"Are 'hello' and 'hello' equal? {are_values_equal('hello', 'hello')}")
    print(f"Are 10 and 11 equal? {are_values_equal(10, 11)}")
    print(f"Are True and True equal? {are_values_equal(True, True)}")
    print(f"Are 3.14 and 3.1400000000000001 equal? {are_values_equal(3.14, 3.1400000000000001)}")
    print(f"Are [1, 2] and [1, 2] equal? {are_values_equal([1, 2], [1, 2])}")
    print(f"Are 'a' and 'b' equal? {are_values_equal('a', 'b')}")