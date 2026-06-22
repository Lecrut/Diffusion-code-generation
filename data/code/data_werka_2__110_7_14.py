from datetime import datetime

def sort_dates(date_strings):
    parsed_dates = []
    for date_str in date_strings:
        parts = date_str.split('-')
        month = int(parts[0])
        day = int(parts[1])
        year = int(parts[2])
        dt = datetime(year, month, day)
        parsed_dates.append((dt, date_str))
    
    parsed_dates.sort(key=lambda x: x[0])
    
    sorted_dates = [item[1] for item in parsed_dates]
    return sorted_dates

if __name__ == '__main__':
    dates = ['12-31-2023', '01-01-2023', '06-15-2022', '02-28-2023']
    result = sort_dates(dates)
    print(result)