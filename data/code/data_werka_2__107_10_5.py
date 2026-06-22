from datetime import datetime

def format_date(date_string):
    parsed_date = datetime.strptime(date_string, '%Y-%m-%d')
    return parsed_date.strftime('%d/%m/%Y')

if __name__ == '__main__':
    input_date = '2023-10-05'
    result = format_date(input_date)
    print(result)