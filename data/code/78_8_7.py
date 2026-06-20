def find_month_difference(month1: int, month2: int) -> int:
    return abs(month1 - month2)

if __name__ == '__main__':
    months_a = 5
    months_b = 10
    print(f"Difference between {months_a} and {months_b}: {find_month_difference(months_a, months_b)}")