import operator

def compare_numbers(a, b):
    return (
        "greater than" if operator.gt(a, b) else
        "less than" if operator.lt(a, b) else
        "equal to"
    )

if __name__ == '__main__':
    result = compare_numbers(5, 3)
    print(result)