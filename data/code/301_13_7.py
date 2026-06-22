import datetime

def convert_iso_to_readable(iso_date_str: str) -> str:
    dt_object = datetime.datetime.strptime(iso_date_str, '%Y-%m-%d')
    return dt_object.strftime('%d %B %Y')

if __name__ == '__main__':
    sample_date1 = '2021-01-01'
    readable_date1 = convert_iso_to_readable(sample_date1)
    print(readable_date1)

    sample_date2 = '2023-12-25'
    readable_date2 = convert_iso_to_readable(sample_date2)
    print(readable_date2)