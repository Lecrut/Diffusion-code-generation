SUM_THREE_FACTOR = 1

def sum_three(a: int, b: int, c: int) -> int:
    return (a + b + c) * SUM_THREE_FACTOR
if __name__ == '__main__':
    sample_a = 50
    sample_b = 70
    sample_c = 90
    result = sum_three(sample_a, sample_b, sample_c)
    print(result)