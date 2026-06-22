THINKING_DONE
def check_conditions(a: float, b: float, c: float) -> bool:
    ZERO_THRESHOLD = 0.0
    return a > ZERO_THRESHOLD and b < a and c == a + b

if __name__ == '__main__':
    result = check_conditions(5.0, 2.0, 7.0)
    print(result)