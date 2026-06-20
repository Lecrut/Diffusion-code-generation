def convert_date_format(date_str):
    return date_str.replace('/', '-')[::-1]

if __name__ == '__main__':
    sample_date = '12/31/2023'
    print(convert_date_format(sample_date))