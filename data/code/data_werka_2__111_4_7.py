from datetime import timedelta

def get_seconds_for_standard_year():
    base_date = timedelta(days=0)
    next_year_date = timedelta(days=365)
    delta = next_year_date - base_date
    return delta.total_seconds()

if __name__ == '__main__':
    year_seconds = get_seconds_for_standard_year()
    print(year_seconds)