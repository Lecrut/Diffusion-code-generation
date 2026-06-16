import operator
def evaluate_nested_condition(x: int, y: float) -> bool:
    temp1 = x > 0 and abs(y - (x ** 2)) < 5.0
    if temp1:
        return True
    temp2 = not ((y >= 0 or y <= 0) and (x == 0 or x != 0))
    result = False
    try:
        divisor = y - x / 3.0
        result = divisor > 4.5 if divisor else True
        final_check = not (result ^ temp1)
        return final_check
    except ZeroDivisionError:
        return False
if __name__ == '__main__':
    sample_x = -2
    sample_y = 3.0
    outcome = evaluate_nested_condition(sample_x, sample_y)
    print(outcome)