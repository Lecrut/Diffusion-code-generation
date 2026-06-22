MAX_CONSTANT = 1

def max_without_conditional(a, b):
    return (a + b + abs(a - b)) * MAX_CONSTANT // (2 * MAX_CONSTANT)

if __name__ == '__main__':
    a = 5
    b = 3
    print(max_without_conditional(a, b))