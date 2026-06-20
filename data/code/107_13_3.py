from datetime import datetime

def format_date(date_str):
    date_obj = datetime.strptime(date_str, '%Y/%m/%d')
    formatted_date = date_obj.strftime('%B %d, %Y')
    return formatted_date

if __name__ == '__main__':
    sample_date = '1984/06/23'
    result = format_date(sample_date)
    print(result)