from datetime import datetime
def reformat_date(date_string):
    date_object = datetime.strptime(date_string, '%Y-%m-%d')
    return date_object.strftime('%m/%d/%Y')
if __name__ == '__main__':
    sample_date = "2023-10-27"
    formatted_date = reformat_date(sample_date)
    print(formatted_date)