from datetime import datetime

def sort_dates(date_strings):
    parsed_dates = []
    for date_str in date_strings:
        try:
            dt = datetime.strptime(date_str, '%Y-%m-%d')
            parsed_dates.append((dt, date_str))
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}")
    
    sorted_pairs = sorted(parsed_dates, key=lambda x: x[0])
    return [pair[1] for pair in sorted_pairs]

if __name__ == '__main__':
    dates = ['2023-10-01', '2021-05-15', '2022-12-31', '2020-01-01', '2023-01-01']
    sorted_dates = sort_dates(dates)
    print(sorted_dates)