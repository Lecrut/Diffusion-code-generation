from datetime import datetime

def format_date(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    formatted_date = date_obj.strftime('%A, %B %d, %Y')
    return formatted_date

if __name__ == '__main__':
    sample_date = '2023-11-15'
    print(format_date(sample_date))