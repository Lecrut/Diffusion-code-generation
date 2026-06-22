from datetime import datetime

def format_dates(date_list):
    for date_str in date_list:
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            formatted_date = date_obj.strftime('%B %d, %Y')
            print(formatted_date)
        except ValueError:
            continue

if __name__ == '__main__':
    sample_dates = ['2023-01-01', '2023-12-25', '2024-07-4']
    format_dates(sample_dates)