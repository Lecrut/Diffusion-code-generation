DIVISION_LIMIT = 400

def check_leap(year: int) -> bool:
    if not isinstance(year, int):
        raise TypeError("Year must be an integer")
    if year < 1:
        raise ValueError("Year must be positive")
    is_div_by_4 = year % 4 == 0
    is_div_by_100 = year % 100 == 0
    is_div_by_400 = year % DIVISION_LIMIT == 0
    if is_div_by_400:
        return True
    if is_div_by_100:
        return False
    return is_div_by_4

if __name__ == '__main__':
    results = [
        check_leap(2024),
        check_leap(1900),
        check_leap(2000),
        check_leap(2023),
        check_leap(2400)
    ]
    for r in results:
        print(r)