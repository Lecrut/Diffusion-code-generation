from datetime import date

DAY_OF_MONTH_OFFSET = 1
EXPECTED_YEAR = 2023
EXPECTED_MONTH = 3
EXPECTED_DAY = 15

def get_day_value(target_date: date) -> int:
    return target_date.day

if __name__ == '__main__':
    sample_date = date(EXPECTED_YEAR, EXPECTED_MONTH, EXPECTED_DAY)
    computed_day = get_day_value(sample_date)
    print(computed_day)