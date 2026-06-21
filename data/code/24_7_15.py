def _divisible_by(a, b):
    return a % b == 0

def is_leap_year(year):
    if not _divisible(year, 4):
        return False
    if _divisible(year, 100) and not _divisible(year, 400):
        return False
    return True

def _divisible(year, divisor):
    return year % divisor == 0

if __name__ == '__main__':
    samples = [2000, 1900, 2024, 2023, 1800, 2400]
    for y in samples:
        print(y, is_leap_year(y))