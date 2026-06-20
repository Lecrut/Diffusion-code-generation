from datetime import date

def get_day_of_month(year, month, day):
    return date(year, month, day).day

if __name__ == '__main__':
    sample_date = (2024, 10, 10)
    print(get_day_of_month(*sample_date))