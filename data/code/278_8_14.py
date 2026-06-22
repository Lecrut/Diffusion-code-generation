from datetime import datetime

def format_dates(date_list):
    formatted_dates = [datetime.strptime(date, '%Y-%m-%d').strftime('%B %d, %Y') for date in date_list]
    return formatted_dates

if __name__ == '__main__':
    sample_dates = ['2023-01-01', '2023-02-14', '2023-12-25']
    print('\n'.join(format_dates(sample_dates)))