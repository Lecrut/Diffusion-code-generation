class LeapYearVerifier:
    def is_leap_year(self, year: int) -> bool:
        if year <= 0:
            raise ValueError("Year must be a positive integer")
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        return False

if __name__ == '__main__':
    verifier = LeapYearVerifier()
    print(verifier.is_leap_year(2000))
    print(verifier.is_leap_year(1900))
    print(verifier.is_leap_year(2024))
    print(verifier.is_leap_year(2023))