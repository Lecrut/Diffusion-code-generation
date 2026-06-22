import datetime
DAYS_OFFSET = 1

def determine_weekday(date_str):
    parsed_date = datetime.date.fromisoformat(date_str)
    return parsed_date.weekday()

if __name__ == '__main__':
    sample_date = '2024-07-04'
    day_index = determine_weekday(sample_date)
    print(day_index)