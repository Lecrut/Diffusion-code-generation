def convert_date_format(date_str):
    DATE_FORMAT_IN = "%m/%d/%Y"
    DATE_FORMAT_OUT = "%Y-%m-%d"
    
    return datetime.datetime.strptime(date_str, DATE_FORMAT_IN).strftime(DATE_FORMAT_OUT)

if __name__ == '__main__':
    sample_date = "12/31/2020"
    converted_date = convert_date_format(sample_date)
    print(converted_date)