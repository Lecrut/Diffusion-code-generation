def date_one_year_later(year, month, day):
    if month == 12:
        new_year = year + 1
        new_month = 1
        new_day = day
    else:
        new_year = year
        new_month = month + 1
        new_day = day
    return (new_year, new_month, new_day)
if __name__ == '__main__':
    date1 = (2023, 10, 26)
    result1 = date_one_year_later(*date1)
    print(f"One year after {date1[0]}-{date1[1]}-{date1[2]} is {result1[0]}-{result1[1]}-{result1[2]}")
    date2 = (2024, 2, 29)
    result2 = date_one_year_later(*date2)
    print(f"One year after {date2[0]}-{date2[1]}-{date2[2]} is {result2[0]}-{result2[1]}-{result2[2]}")
    date3 = (2023, 12, 31)
    result3 = date_one_year_later(*date3)
    print(f"One year after {date3[0]}-{date3[1]}-{date3[2]} is {result3[0]}-{result3[1]}-{result3[2]}")
    date4 = (2024, 1, 15)
    result4 = date_one_year_later(*date4)
    print(f"One year after {date4[0]}-{date4[1]}-{date4[2]} is {result4[0]}-{result4[1]}-{result4[2]}")