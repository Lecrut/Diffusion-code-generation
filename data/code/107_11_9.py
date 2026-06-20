def convert_date_format(date_str):
    return date_str.split('/')[2] + '-' + date_str.split('/')[0] + '-' + date_str.split('/')[1]

if __name__ == '__main__':
    print(convert_date_format('12/31/2020'))