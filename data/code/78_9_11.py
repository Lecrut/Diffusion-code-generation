def calculate_month_difference(start_month: int, end_month: int) -> int:
    return abs(end_month - start_month)

if __name__ == '__main__':
    month_a = 7
    month_b = 2
    difference = calculate_month_difference(month_a, month_b)
    print(difference)