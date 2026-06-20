TRUE = True

def are_strictly_true(a, b):
    return bool(a) and bool(b)

if __name__ == '__main__':
    print(are_strictly_true(TRUE, TRUE))
    print(are_strictly_true(FALSE, TRUE))
    print(are_strictly_true(TRUE, FALSE))
    print(are_strictly_true(FALSE, FALSE))