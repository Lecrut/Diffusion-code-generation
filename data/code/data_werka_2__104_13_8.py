import datetime

def is_week_match(d1: datetime.date, d2: datetime.date) -> bool:
    iso_1 = d1.isocalendar()
    iso_2 = d2.isocalendar()
    return iso_1[0] == iso_2[0] and iso_1[1] == iso_2[1]

if __name__ == '__main__':
    dates = {
        "start": datetime.date(2023, 1, 1),
        "mid": datetime.date(2023, 1, 4),
        "boundary": datetime.date(2023, 1, 8),
        "prev_year": datetime.date(2022, 12, 31),
    }
    print(is_week_match(dates["start"], dates["mid"]))
    print(is_week_match(dates["start"], dates["boundary"]))
    print(is_week_match(dates["start"], dates["prev_year"]))