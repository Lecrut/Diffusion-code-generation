def are_equal(x, y):
    return x == y
if __name__ == '__main__':
    a = 10
    b = 10
    c = "hello"
    d = "world"
    e = [1, 2]
    f = [1, 2]
    g = (1, 2)
    h = (1, 2)
    print(f"a == b: {are_equal(a, b)}")
    print(f"c == d: {are_equal(c, d)}")
    print(f"e == f: {are_equal(e, f)}")
    print(f"g == h: {are_equal(g, h)}")
    print(f"a == c: {are_equal(a, c)}")
    print(f"e == g: {are_equal(e, g)}")