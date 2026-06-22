from datetime import datetime
from typing import Dict

DATE_FORMATS: Dict[str, str] = {
    'DD-MM-YYYY HH:MM:SS': '%d-%m-%Y %H:%M:%S',
}

ISO_FORMAT: str = '%Y-%m-%dT%H:%M:%S'

def convert_date(input_date: str, input_format: str = '%d-%m-%Y %H:%M:%S') -> str:
    parsed_date = datetime.strptime(input_date, input_format)
    return parsed_date.strftime(ISO_FORMAT)

if __name__ == '__main__':
    sample_date = '15-08-2024 09:15:30'
    result = convert_date(sample_date)
    print(result)