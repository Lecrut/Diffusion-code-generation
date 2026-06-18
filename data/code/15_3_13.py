def is_equal(x: any, y: any) -> bool:
    return x == y

if __name__ == '__main__':
    assert (is_equal(10, 20)) == False and (is_equal("hello", "hello")) == True