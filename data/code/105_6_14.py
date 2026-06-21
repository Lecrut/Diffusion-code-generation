from datetime import date, timedelta

START_DATE = date(2024, 1, 1)
MULTIPLE_OF = 7

def get_next_seven_day_date():
    current = START_DATE
    days_elapsed = 0
    while True:
        days_elapsed += 1
        current += timedelta(days=1)
        if days_elapsed % MULTIPLE_OF == 0:
            return current

if __name__ == '__main__':
    print(get_next_seven_day_date())