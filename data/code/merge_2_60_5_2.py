def check_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return year % 4 == 0
if __name__ == '__main__':
    test_years = [2000, 1900, 2024, 2023]
    print(f"Is {test_years[0]} a leap year? ", end="")
    result_1 = check_leap_year(test_years[0])
    print(f"Is {test_years[1]} a leap year? ", end="")
    result_2 = check_leap_year(test_years[1])
    print(f"Is {test_years[2]} a leap year? ", end="")
    result_3 = check_leap_year(test_years[2])
    print(f"Is {test_years[3]} a leap year? ", end="")
    result_4 = check_leap_year(test_years[3])
    if result_1:
        print("Yes")
    else:
        print("No")
    if result_2:
        print("Yes")
    else:
        print("No")
    if result_3:
        print("Yes")
    else:
        print("No")
    if result_4:
        print("Yes")
    else:
        print("No")