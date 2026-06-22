from collections import namedtuple

LeapResult = namedtuple("LeapResult", "year is_leap")

def check_leap(year):
    if year < 1:
        raise ValueError("Year must be positive")
    div_by_4 = year % 4 == 0
    div_by_100 = year % 100 == 0
    div_by_400 = year % 400 == 0
    if div_by_400:
        return LeapResult(year, True)
    if div_by_100:
        return LeapResult(year, False)
    if div_by_4:
        return LeapResult(year, True)
    return LeapResult(year, False)

if __name__ == '__main__':
    samples = [1600, 1700, 2024]
    for y in samples:
        result = check_leap(y)
        print(f"Year {result.year} is leap: {result.is_leap}")