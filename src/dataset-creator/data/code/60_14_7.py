def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if __name__ == '__main__':
    samples = [2000, 2023, 1900]
    for sample in samples:
        result = is_leap_year(sample)
        print(f"{sample}: {result}")