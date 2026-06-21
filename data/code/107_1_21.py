from datetime import datetime

def convert_date(date_string):
    parsed_date = datetime.strptime(date_string, '%m/%d/%Y')
    return parsed_date.strftime('%d-%m-%Y')

if __name__ == '__main__':
    sample_date = '12/25/2023'
    result = convert_date(sample_date)
    print(result)