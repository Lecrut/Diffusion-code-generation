from datetime import datetime

def format_date(date_string: str) -> str:
    dt = datetime.strptime(date_string, '%Y/%m/%d')
    return dt.strftime('%B %d, %Y')

if __name__ == '__main__':
    result = format_date('2023/10/05')
    print(result)