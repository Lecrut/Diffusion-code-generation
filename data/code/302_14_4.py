import datetime
def get_day_of_month(year, month):
    try:
        date = datetime.date(year, month, 1)
        return date.day
    except ValueError as e:
        return f"Invalid date: {e}"
if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    result = get_day_of_month(sample_year, sample_month)
    print(result)