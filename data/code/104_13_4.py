import datetime

def same_week(date_a: datetime.date, date_b: datetime.date) -> bool:
    iso_a = date_a.isocalendar()
    iso_b = date_b.isocalendar()
    return (iso_a[0], iso_a[1]) == (iso_b[0], iso_b[1])

if __name__ == '__main__':
    sample_dates = {
        "monday": datetime.date(2024, 1, 1),
        "sunday": datetime.date(2024, 1, 7),
        "next_monday": datetime.date(2024, 1, 8),
        "last_year": datetime.date(2023, 12, 31),
    }
    d1 = sample_dates["monday"]
    d2 = sample_dates["sunday"]
    d3 = sample_dates["next_monday"]
    d4 = sample_dates["last_year"]
    print(same_week(d1, d2))
    print(same_week(d1, d3))
    print(same_week(d1, d4))