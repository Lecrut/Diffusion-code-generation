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
    i = {'a': 1}
    j = {'a': 1}
    k = [1, 2]
    l = [3, 4]
    print(f"a == b: {are_equal(a, b)}")
    print(f"c == d: {are_equal(c, d)}")
    print(f"e == f: {are_equal(e, f)}")
    print(f"g == h: {are_equal(g, h)}")
    print(f"i == j: {are_equal(i, j)}")
    print(f"k == l: {are_equal(k, l)}")