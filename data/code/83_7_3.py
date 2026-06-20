from datetime import date

def compare_dates(date1: date, date2: date) -> str:
    if date1 < date2:
        return "date1 is earlier than date2"
    elif date1 > date2:
        return "date1 is later than date2"
    else:
        return "date1 and date2 are the same"

if __name__ == '__main__':
    sample_date1 = date(2023, 10, 5)
    sample_date2 = date(2023, 9, 15)
    print(compare_dates(sample_date1, sample_date2))