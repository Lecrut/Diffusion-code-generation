from typing import final

@final
class LeapYearVerifier:

    @staticmethod
    def is_leap(year: int) -> bool:
        if year <= 0:
            return False
        if year % 4 != 0:
            return False
        if year % 100 != 0:
            return True
        if year % 400 != 0:
            return False
        return True
if __name__ == '__main__':
    verifier = LeapYearVerifier()
    test_years = [2000, 1900, 2024, 2023, 4, 100, 400, -5, 0]
    results = []
    for y in test_years:
        results.append(f'{y}: {verifier.is_leap(y)}')
    print('\n'.join(results))