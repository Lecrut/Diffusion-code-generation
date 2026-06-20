from datetime import datetime

def convert_date_format(date_str):
    date_obj = datetime.strptime(date_str, '%m/%d/%Y')
    return date_obj.strftime('%d-%m-%Y')

if __name__ == '__main__':
    sample_date = '12/31/2023'
    converted_date = convert_date_format(sample_date)
    print(converted_date)