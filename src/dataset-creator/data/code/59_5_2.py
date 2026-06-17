from datetime import date
def get_weekday(date: date) -> str:
    return date.strftime("%A")
if __name__ == '__main__':
    sample_date = date(2023, 10, 5)
    print(get_weekday(sample_date))