from datetime import datetime
def format_date(dt_object):
    month = dt_object.strftime('%B')
    day = dt_object.strftime('%d')
    year = dt_object.strftime('%Y')
    return f"{month} {day}, {year}"
if __name__ == '__main__':
    sample_date = datetime(2023, 1, 1)
    formatted_string = format_date(sample_date)
    print(formatted_string)
    sample_date_2 = datetime(2024, 5, 15)
    formatted_string_2 = format_date(sample_date_2)
    print(formatted_string_2)