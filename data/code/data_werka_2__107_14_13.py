from datetime import datetime

DATE_FORMATS = {
    'DD-MM-YYYY HH:MM:SS': '%d-%m-%Y %H:%M:%S',
    'YYYY-MM-DDTHH:MM:SS': '%Y-%m-%dT%H:%M:%S'
}

def convert_date_format(date_string: str) -> str:
    source_format = DATE_FORMATS['DD-MM-YYYY HH:MM:SS']
    parsed_date = datetime.strptime(date_string, source_format)
    target_format = DATE_FORMATS['YYYY-MM-DDTHH:MM:SS']
    return parsed_date.strftime(target_format)

if __name__ == '__main__':
    sample_date = '15-08-2024 09:15:30'
    iso_date = convert_date_format(sample_date)
    print(iso_date)