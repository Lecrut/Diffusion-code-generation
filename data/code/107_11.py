import datetime
def format_date_string(iso_date_string):
    dt_object = datetime.datetime.strptime(iso_date_string, '%Y-%m-%d')
    return dt_object.strftime('%m/%d/%Y')
if __name__ == '__main__':
    sample_date = "2023-10-27"
    formatted_date = format_date_string(sample_date)
    print(formatted_date)