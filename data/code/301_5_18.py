from datetime import datetime

def convert_to_iso_format(date_str):
    dt_object = datetime.strptime(date_str, '%d/%m/%Y %I:%M %p')
    iso_formatted_date = dt_object.strftime('%Y-%m-%dT%H:%M:00')
    return iso_formatted_date

if __name__ == '__main__':
    sample_date = '15/08/2023 04:30 PM'
    result = convert_to_iso_format(sample_date)
    print(result)