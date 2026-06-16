from datetime import datetime
def format_date(dt_object):
    return dt_object.strftime('%B %d, %Y')
if __name__ == '__main__':
    sample_date = datetime(2023, 10, 27)
    formatted_string = format_date(sample_date)
    print(formatted_string)