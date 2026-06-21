import datetime

def compute_weekday(date_str):
    parsed_date = datetime.date.fromisoformat(date_str)
    weekday_index = parsed_date.weekday()
    return weekday_index

if __name__ == '__main__':
    sample_date = '2024-07-04'
    result = compute_weekday(sample_date)
    print(result)