from datetime import datetime

DATE_INPUT_FORMAT = '%m/%d/%Y'
DATE_OUTPUT_FORMAT = '%d-%m-%Y'

INPUT_TO_OUTPUT_MAP = {
    '01/01/2023': '01-01-2023',
    '12/31/2023': '31-12-2023',
    '02/29/2024': '29-02-2024',
}

def transform_date(source: str) -> str:
    parsed = datetime.strptime(source, DATE_INPUT_FORMAT)
    return parsed.strftime(DATE_OUTPUT_FORMAT)

if __name__ == '__main__':
    test_cases = ['10/05/2022', '01/15/2024', '07/20/2020']
    for entry in test_cases:
        computed = transform_date(entry)
        print(computed)