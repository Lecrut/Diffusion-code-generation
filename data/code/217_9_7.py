import operator

def compare_integers(a, b):
    return (
        "greater than" if operator.gt(a, b) else
        "less than" if operator.lt(a, b) else
        "equal to"
    )

if __name__ == '__main__':
    result = compare_integers(5, 3)
    print(result)