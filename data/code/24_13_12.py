class LeapYearVerifier:
    def is_leap_year(self, year: int) -> bool:
        if year < 1:
            return False
        if year % 4 == 0:
            if year % 100 == 0:
                return year % 400 == 0
            return True
        return False

if __name__ == '__main__':
    verifier = LeapYearVerifier()
    sample_years = [2000, 1900, 2024, 2023, 0, -4]
    for year in sample_years:
        result = verifier.is_leap_year(year)
        print(f"{year}: {result}")