import math

def compare_lengths(a: float, b: float) -> tuple:
    diff = abs(a - b)
    if diff < 1e-9:
        length_type = "equal"
    elif a > b:
        length_type = "a is greater"
    else:
        length_type = "b is greater"
    return (diff, length_type)

if __name__ == '__main__':
    result = compare_lengths(5.5, 3.2)
    print(result)