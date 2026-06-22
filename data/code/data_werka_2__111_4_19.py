from datetime import timedelta

def calculate_seconds_in_year(year: int) -> int:
    start = timedelta(days=365)
    end = timedelta(days=0)
    diff = start - end
    return int(diff.total_seconds())

if __name__ == '__main__':
    result = calculate_seconds_in_year(2023)
    print(result)