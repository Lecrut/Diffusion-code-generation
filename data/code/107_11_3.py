def convert_date_format(date_str):
    return '-'.join(reversed(date_str.split('/')))

if __name__ == '__main__':
    print(convert_date_format('09/15/2023'))