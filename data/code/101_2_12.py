def get_day_of_week(year: int, month: int, day: int) -> int:
    if year < 1753:
        raise ValueError('Year must be 1753 or later.')
    if month < 3:
        month += 12
        year -= 1
    q = day
    m = month
    k = year % 100
    j = year // 100
    f = q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 - 2 * j
    day_index = f % 7
    return day_index
if __name__ == '__main__':
    sample_date = (2024, 2, 29)
    print(f'Date: {sample_date}, Day Index (Monday=0): {get_day_of_week(*sample_date)}')