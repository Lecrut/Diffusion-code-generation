import datetime

def retrieve_weekday_index(date_str):
    parsed_date = datetime.date.fromisoformat(date_str)
    return parsed_date.weekday()

if __name__ == '__main__':
    sample_date = '2024-07-04'
    computed_index = retrieve_weekday_index(sample_date)
    print(computed_index)