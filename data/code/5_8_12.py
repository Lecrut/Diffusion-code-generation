import math

def compare_lengths(a: float, b: float) -> tuple:
    diff = abs(a - b)
    if math.isnan(diff):
        desc = "Both lengths are invalid"
    elif diff == 0:
        desc = "Lengths are equal"
    elif a > b:
        desc = "First length is greater"
    else:
        desc = "Second length is greater"
    return (diff, desc)

if __name__ == '__main__':
    a_val = 10.5
    b_val = 7.2
    result = compare_lengths(a_val, b_val)
    print(result)