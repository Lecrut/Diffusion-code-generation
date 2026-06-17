from datetime import date
def get_weekday(date: date) -> int:
    return date.weekday()
if __name__ == '__main__':
    sample_date = date(2023, 10, 5)
    result = get_weekday(sample_date)
    print(result)