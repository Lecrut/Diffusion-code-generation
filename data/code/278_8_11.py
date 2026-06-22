from datetime import datetime

def format_dates(date_list):
    for date_str in date_list:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        print(date_obj.strftime('%B %d, %Y'))

if __name__ == '__main__':
    sample_dates = ['2023-01-01', '2023-12-25', '2024-07-04']
    format_dates(sample_dates)