import datetime

def sort_date_strings(date_list):
    date_to_obj = {}
    for date_str in date_list:
        try:
            date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
            date_to_obj[date_str] = date_obj
        except ValueError:
            continue
    sorted_dates = [date for date, _ in sorted(date_to_obj.items(), key=lambda item: item[1])]
    return sorted_dates

if __name__ == '__main__':
    sample_dates = ['2023-01-01', '2022-12-31', '2023-04-01']
    sorted_dates = sort_date_strings(sample_dates)
    print(sorted_dates)