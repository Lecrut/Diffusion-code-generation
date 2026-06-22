from datetime import datetime
INPUT_FORMAT = '%m/%d/%Y'
OUTPUT_FORMAT = '%Y-%m-%d'

def convert_date(date_str):
    dt_object = datetime.strptime(date_str, INPUT_FORMAT)
    return dt_object.strftime(OUTPUT_FORMAT)
if __name__ == '__main__':
    sample_dates = ['10/27/2023', '01/01/2024', '12/31/2025']
    converted_dates = [convert_date(date) for date in sample_dates]
    print(converted_dates)