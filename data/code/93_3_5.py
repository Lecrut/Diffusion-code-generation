FALSE = False

def both_false(x, y):
    return not x and not y

if __name__ == '__main__':
    print(both_false(FALSE, FALSE))
    print(both_false(TRUE, FALSE))
    print(both_false(FALSE, TRUE))
    print(both_false(TRUE, TRUE))