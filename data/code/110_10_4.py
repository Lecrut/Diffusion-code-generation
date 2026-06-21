from datetime import datetime

def parse_date(date_str):
    year_str = date_str[:4]
    month_str = date_str[5:7]
    day_str = date_str[8:10]
    return datetime(int(year_str), int(month_str), int(day_str))

def sort_dates(date_strings):
    parsed_dates = []
    for date_str in date_strings:
        parsed_dates.append(parse_date(date_str))
    sorted_pairs = sorted(zip(parsed_dates, date_strings))
    result = [pair[1] for pair in sorted_pairs]
    return result

if __name__ == '__main__':
    unsorted = ['2000-01-01', '2020-12-31', '1999-02-28', '2020-01-02']
    sorted_list = sort_dates(unsorted)
    print(sorted_list)