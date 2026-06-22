ZERO = 0.0

def check_conditions(first: float, second: float, third: float) -> bool:
    is_positive = first > ZERO
    is_ordered = second < first
    is_sum = third == (first + second)
    return is_positive and is_ordered and is_sum

if __name__ == '__main__':
    val1 = 10.5
    val2 = 3.2
    val3 = 13.7
    output = check_conditions(val1, val2, val3)
    print(output)