import datetime

def sort_date_strings(date_strings):
    parsed_dates = []
    for date_str in date_strings:
        try:
            parsed = datetime.datetime.strptime(date_str, '%m-%d-%Y')
            parsed_dates.append(parsed)
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}")
    
    sorted_dates = sorted(parsed_dates)
    return [date.strftime('%m-%d-%Y') for date in sorted_dates]

if __name__ == '__main__':
    sample_dates = ['01-05-2023', '12-31-2022', '07-04-2021']
    sorted_sample_dates = sort_date_strings(sample_dates)
    print(sorted_sample_dates)