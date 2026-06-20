def find_month_difference(month1: int, month2: int) -> int:
    return abs(month1 - month2)

if __name__ == '__main__':
    sample_months_a = 5
    sample_months_b = 10
    print(f"Difference between {sample_months_a} and {sample_months_b}: {find_month_difference(sample_months_a, sample_months_b)}")