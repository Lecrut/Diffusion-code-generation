def get_later_date(date_a: str, date_b: str) -> str:
    year_a = int(date_a[0:4])
    month_a = int(date_a[5:7])
    day_a = int(date_a[8:10])
    year_b = int(date_b[0:4])
    month_b = int(date_b[5:7])
    day_b = int(date_b[8:10])
    if year_a > year_b:
        return date_a
    if year_a < year_b:
        return date_b
    if month_a > month_b:
        return date_a
    if month_a < month_b:
        return date_b
    if day_a > day_b:
        return date_a
    return date_b
if __name__ == '__main__':
    sample_a = "1999-01-01"
    sample_b = "1998-12-31"
    final_date = get_later_date(sample_a, sample_b)
    print(final_date)