import operator

def compare_integers(a, b):
    return (
        operator.gt(a, b),
        operator.lt(a, b),
        operator.eq(a, b)
    )

if __name__ == '__main__':
    result = compare_integers(5, 3)
    print(f"Greater than: {result[0]}, Less than: {result[1]}, Equal to: {result[2]}")