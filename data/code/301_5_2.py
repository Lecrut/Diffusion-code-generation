from datetime import datetime
def convert_iso_to_date_ymd(iso_date_str):
    dt_object = datetime.strptime(iso_date_str, '%Y-%m-%dT%H:%M:%S')
    formatted_date = dt_object.strftime('%Y/%m/%d')
    return formatted_date
if __name__ == '__main__':
    iso_input = '2023-10-27T14:30:00'
    result = convert_iso_to_date_ymd(iso_input)
    print(result)