def evaluate_conditions(a: int, b: int, c: int) -> bool:
    positives = 0
    if a > 0:
        positives += 1
    if positives >= 2:
        return True
    if b > 0:
        positives += 1
    if positives >= 2:
        return True
    if c > 0:
        positives += 1
    return positives >= 2

if __name__ == '__main__':
    val1 = evaluate_conditions(10, -5, 20)
    print(val1)
    val2 = evaluate_conditions(-1, -2, -3)
    print(val2)
    val3 = evaluate_conditions(0, 0, 1)
    print(val3)