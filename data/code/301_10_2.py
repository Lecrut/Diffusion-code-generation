from datetime import datetime

def convert_date_format(date_str):
    return date_str[:4] + '-' + date_str[5:7] + '-' + date_str[8:]

if __name__ == '__main__':
    sample_date = '2023-10-05'
    converted_date = convert_date_format(sample_date)
    print(converted_date)