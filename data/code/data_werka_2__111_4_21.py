from datetime import timedelta

def calculate_seconds_in_year(year: int) -> int:
    start = (year, 1, 1)
    end = (year + 1, 1, 1)
    start_date = timedelta(days=0).replace(year=start[0], month=start[1], day=start[2])
    end_date = timedelta(days=0).replace(year=end[0], month=end[1], day=end[2])
    delta = end_date - start_date
    total_seconds = int(delta.total_seconds())
    return total_seconds

if __name__ == '__main__':
    year = 2023
    result = calculate_seconds_in_year(year)
    print(result)