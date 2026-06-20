from datetime import date

def get_day_of_month(year, month, day):
    try:
        return date(year, month, day).day
    except ValueError as e:
        print(f"Invalid date: {e}")
        raise

if __name__ == '__main__':
    sample_year = 2024
    sample_month = 10
    sample_day = 10
    print(get_day_of_month(sample_year, sample_month, sample_day))