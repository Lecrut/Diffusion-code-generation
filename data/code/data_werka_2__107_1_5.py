from datetime import datetime

def convert_date(date_string):
    parsed_date = datetime.strptime(date_string, '%m/%d/%Y')
    formatted_date = parsed_date.strftime('%d-%m-%Y')
    return formatted_date

if __name__ == '__main__':
    original_date = '12/31/2023'
    result = convert_date(original_date)
    print(result)