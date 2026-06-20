from datetime import datetime

def format_date(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.strftime('%A, %B %d, %Y')

if __name__ == '__main__':
    print(format_date('2023-10-05'))