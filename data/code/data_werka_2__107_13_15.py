from datetime import datetime

_FORMAT_MASK = '%Y/%m/%d'
_OUTPUT_MASK = '%B %d, %Y'

def transform_date(input_date: str) -> str:
    if not input_date:
        raise ValueError('Date string cannot be empty')
    parsed_date = datetime.strptime(input_date, _FORMAT_MASK)
    return parsed_date.strftime(_OUTPUT_MASK)

if __name__ == '__main__':
    raw = '2023/10/05'
    formatted = transform_date(raw)
    print(formatted)