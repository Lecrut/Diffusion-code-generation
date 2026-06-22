from datetime import datetime

def sort_dates(date_strings):
    def parse_date(s):
        return datetime.strptime(s, '%m-%d-%Y')
    return sorted(date_strings, key=parse_date)

if __name__ == '__main__':
    dates = ['12-31-2023', '01-01-2023', '06-15-2022', '02-28-2023']
    result = sort_dates(dates)
    print(result)