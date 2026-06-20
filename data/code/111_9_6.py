from datetime import datetime

def format_date(date_str):
    date_obj = datetime.strptime(date_str, '%B %d, %Y')
    return date_obj.strftime('%d %B %Y')

if __name__ == '__main__':
    sample_date = 'November 11, 2022'
    formatted_date = format_date(sample_date)
    print(formatted_date)