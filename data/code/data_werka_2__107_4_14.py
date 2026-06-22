from datetime import datetime

INPUT_FORMAT = "%d.%m.%Y"
OUTPUT_FORMAT = "%Y-%m-%d"
SAMPLE_DATES = ["25.12.2023", "01.01.2000", "31.12.1999"]

def transform_date(date_str: str) -> str:
    dt_object = datetime.strptime(date_str, INPUT_FORMAT)
    return dt_object.strftime(OUTPUT_FORMAT)

if __name__ == '__main__':
    for sample in SAMPLE_DATES:
        result = transform_date(sample)
        print(result)