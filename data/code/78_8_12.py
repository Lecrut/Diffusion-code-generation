def find_month_difference(month1: int, month2: int) -> int:
    return abs(month1 - month2)

if __name__ == '__main__':
    sample_months_1 = 4
    sample_months_2 = 9
    sample_months_3 = 11
    sample_months_4 = 2

    print(f"Difference between {sample_months_1} and {sample_months_2}: {find_month_difference(sample_months_1, sample_months_2)}")
    print(f"Difference between {sample_months_2} and {sample_months_3}: {find_month_difference(sample_months_2, sample_months_3)}")
    print(f"Difference between {sample_months_3} and {sample_months_4}: {find_month_difference(sample_months_3, sample_months_4)}")