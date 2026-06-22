import datetime

def convert_date(date_string):
    parsed_date = datetime.datetime.strptime(date_string, '%m/%d/%Y')
    return parsed_date.strftime('%Y-%m-%d')

if __name__ == '__main__':
    sample_date = '12/31/2023'
    result = convert_date(sample_date)
    print(result)