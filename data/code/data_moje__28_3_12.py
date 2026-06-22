LOWER_BOUND = -float('inf')
UPPER_BOUND = float('inf')

def sort_two_floats(a, b):
    first = a if a < b else b
    second = b if a < b else a
    return (first, second)

if __name__ == '__main__':
    val1 = 42.5
    val2 = 10.1
    print(sort_two_floats(val1, val2))