from datetime import datetime

def sort_date_strings(date_strings):
    def parse_date(date_str):
        return datetime.strptime(date_str, '%m-%d-%Y')
    
    return sorted(date_strings, key=parse_date)

if __name__ == '__main__':
    dates = ['12-31-2023', '01-01-2023', '06-15-2022', '02-28-2023']
    sorted_dates = sort_date_strings(dates)
    print(sorted_dates)