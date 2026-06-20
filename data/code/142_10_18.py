TRUE = True
FALSE = False

def are_booleans_equal(a, b):
    return (not a) == (not b)

if __name__ == '__main__':
    print(are_booleans_equal(TRUE, TRUE))
    print(are_booleans_equal(FALSE, FALSE))
    print(are_booleans_equal(TRUE, FALSE))