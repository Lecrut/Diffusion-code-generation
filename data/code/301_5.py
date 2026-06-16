from datetime import datetime
def convert_iso_to_ymd(iso_date_str):
    dt_object = datetime.strptime(iso_date_str, '%Y-%m-%dT%H:%M:%S')
    ymd_date_str = dt_object.strftime('%Y/%m/%d')
    return ymd_date_str
if __name__ == '__main__':
    sample_date = '2023-10-27T14:30:00'
    result = convert_iso_to_ymd(sample_date)
    print(result)