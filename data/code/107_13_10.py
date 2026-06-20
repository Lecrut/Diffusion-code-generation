from datetime import datetime

def format_date(date_str):
    date_obj = datetime.strptime(date_str, '%Y/%m/%d')
    return date_obj.strftime('%B %d, %Y')

if __name__ == '__main__':
    sample_date = '2023/11/15'
    formatted_date = format_date(sample_date)
    print(formatted_date)