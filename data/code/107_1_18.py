from datetime import datetime

def transform_date_format(source: str) -> str:
    dt_obj = datetime.strptime(source, '%m/%d/%Y')
    return dt_obj.strftime('%d-%m-%Y')

if __name__ == '__main__':
    input_date = '07/04/2021'
    converted = transform_date_format(input_date)
    print(converted)