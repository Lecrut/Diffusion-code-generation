from datetime import date

def same_week(date1: date, date2: date) -> bool:
    return date1.isocalendar()[1] == date2.isocalendar()[1]

if __name__ == '__main__':
    sample_date1 = date(2023, 4, 15)
    sample_date2 = date(2023, 4, 22)
    print(same_week(sample_date1, sample_date2))