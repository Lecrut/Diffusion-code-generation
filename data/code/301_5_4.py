from datetime import datetime

def convert_date_format(date_str):
    return date_str.replace(' ', 'T').replace('/', '-').replace(' AM', ':00Z').replace(' PM', ':00Z')

if __name__ == '__main__':
    sample_date = "12/31/2020 11:59 PM"
    print(convert_date_format(sample_date))