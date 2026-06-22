import datetime

WEEK_START_OFFSET = 0
WEEK_END_OFFSET = 6
ISO_WEEK_INDEX = 1
ISO_YEAR_INDEX = 0

def is_same_week_iso(date_a: datetime.date, date_b: datetime.date) -> bool:
    iso_a = date_a.isocalendar()
    iso_b = date_b.isocalendar()
    return iso_a[ISO_YEAR_INDEX] == iso_b[ISO_YEAR_INDEX] and iso_a[ISO_WEEK_INDEX] == iso_b[ISO_WEEK_INDEX]

if __name__ == '__main__':
    start_of_week = datetime.date(2024, 1, 1)
    end_of_week = datetime.date(2024, 1, 7)
    next_week_start = datetime.date(2024, 1, 8)
    
    result_same = is_same_week_iso(start_of_week, end_of_week)
    result_diff = is_same_week_iso(start_of_week, next_week_start)
    
    print(result_same)
    print(result_diff)