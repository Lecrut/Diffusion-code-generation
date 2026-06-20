from datetime import date, timedelta

TUESDAY = 1
JULY_4_2023 = date(2023, 7, 4)

def get_next_tuesday(start_date: date) -> date:
    days_until_tuesday = (TUESDAY - start_date.weekday()) % 7
    return start_date + timedelta(days=days_until_tuesday)

if __name__ == '__main__':
    sample_date = JULY_4_2023
    result = get_next_tuesday(sample_date)
    print(result.strftime('%Y-%m-%d'))