from datetime import datetime

def format_dates(date_list):
    formatted_dates = []
    for date_str in date_list:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        formatted_date = date_obj.strftime('%B %d, %Y')
        formatted_dates.append(formatted_date)
    return formatted_dates

if __name__ == '__main__':
    sample_dates = ['2023-01-01', '2023-12-25']
    formatted_sample_dates = format_dates(sample_dates)
    for date in formatted_sample_dates:
        print(date)