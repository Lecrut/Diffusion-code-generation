import datetime

def sort_date_strings(date_strings):
    parsed_dates = []
    try:
        for date_str in date_strings:
            parsed_date = datetime.datetime.strptime(date_str, '%m-%d-%Y')
            parsed_dates.append(parsed_date)
        parsed_dates.sort()
        sorted_date_strings = [parsed_date.strftime('%m-%d-%Y') for parsed_date in parsed_dates]
        return sorted_date_strings
    except ValueError as e:
        raise ValueError("Invalid date format. Please use 'MM-DD-YYYY'.")
if __name__ == '__main__':
    sample_dates = ['01-25-2022', '12-31-2021', '07-04-2023']
    sorted_dates = sort_date_strings(sample_dates)
    print(sorted_dates)