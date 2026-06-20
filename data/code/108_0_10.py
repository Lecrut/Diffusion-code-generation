from datetime import date

def get_day_of_month(year, month, day):
    specific_date = date(year, month, day)
    return specific_date.day

if __name__ == '__main__':
    print(get_day_of_month(2023, 10, 5))