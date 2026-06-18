import datetime
def get_weekday(date: datetime.date) -> str:
    return date.strftime("%A")
if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 5)
    result = get_weekday(sample_date)
    print(result)