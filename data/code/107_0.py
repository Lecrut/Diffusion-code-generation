import datetime
def reformat_date(date_str):
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.strftime('%m/%d/%Y')
if __name__ == '__main__':
    sample_date = "2023-10-27"
    formatted_date = reformat_date(sample_date)
    print(formatted_date)