from datetime import datetime

def convert_date_format(date_str):
    return date_str.replace(' ', 'T').replace('/', '-').replace(' AM', '').replace(' PM', ':00')

if __name__ == '__main__':
    sample_date = "15/08/2023 04:30 PM"
    converted_date = convert_date_format(sample_date)
    print(converted_date)