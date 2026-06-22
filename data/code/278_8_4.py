from datetime import datetime

def format_dates(date_list):
    return [datetime.strptime(date, '%Y-%m-%d').strftime('%B %d, %Y') for date in date_list]

if __name__ == '__main__':
    sample_dates = ['2023-01-01', '2023-12-25', '2024-07-04']
    formatted_dates = format_dates(sample_dates)
    for date in formatted_dates:
        print(date)