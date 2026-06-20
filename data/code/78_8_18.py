def find_month_difference(month1: int, month2: int) -> int:
    return abs(month1 - month2)

if __name__ == '__main__':
    sample_months_a = (1, 5)
    sample_months_b = (12, 3)
    sample_months_c = (7, 7)
    
    print(f"Difference between {sample_months_a}: {find_month_difference(*sample_months_a)}")
    print(f"Difference between {sample_months_b}: {find_month_difference(*sample_months_b)}")
    print(f"Difference between {sample_months_c}: {find_month_difference(*sample_months_c)}")