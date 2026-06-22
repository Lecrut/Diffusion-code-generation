from datetime import datetime
INPUT_FORMAT = '%d-%m-%Y'
OUTPUT_FORMAT = '%A, %B %d, %Y'

def date_to_string(date_object):
    try:
        converted_date = date_object.strftime(OUTPUT_FORMAT)
        return converted_date
    except AttributeError as e:
        return f'Error: Invalid datetime object. Details: {e}'
if __name__ == '__main__':
    sample_date1 = datetime.strptime('31-12-2023', INPUT_FORMAT)
    sample_date2 = datetime.strptime('05/06/2024', '%m/%d/%Y')
    result1 = date_to_string(sample_date1)
    print(f'Input: 31-12-2023 ({INPUT_FORMAT}) -> Output: {result1}')
    result2 = date_to_string(sample_date2)
    print(f'Input: 05/06/2024 (%m/%d/%Y) -> Output: {result2}')