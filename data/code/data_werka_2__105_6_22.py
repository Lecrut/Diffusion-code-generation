from datetime import date, timedelta

SEVEN_DAYS = 7
START_DATE = date(2024, 1, 1)

def find_next_seven_day_marker() -> date:
    marker_date = START_DATE + timedelta(days=SEVEN_DAYS)
    return marker_date

if __name__ == '__main__':
    result = find_next_seven_day_marker()
    print(result)