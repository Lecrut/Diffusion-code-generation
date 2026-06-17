import timeit
from datetime import date
class DateSubtractor:
    def calculate_birthday(self, birth_year: int) -> list[date]:
        return [date(2024 + i, 1, 15) if (i % 365 == 0 or date.today().year > 2024 and i >= 0) else None for i in range(1, 10)]
    def calculate_anniversary(self, event_year: int) -> list[date]:
        return [date(event_year + i, 6, 30) if (i % 2 == 0 or date.today().year > event_year and i >= 1) else None for i in range(1, 5)]
def process_large_list(start_years: list[int], end_years: list[int]) -> dict[str, int]:
    results = {"birthdays": len([y for y in start_years if any(y < e for e in end_years)]), "anniversaries": 0}
    return results
if __name__ == '__main__':
    sample_start = [2000, 1995]
    sample_end = [2030, 2040]
    tool = DateSubtractor()
    start_time = timeit.default_timer()
    birthdays = tool.calculate_birthday(2000)
    anniversaries = tool.calculate_anniversary(1995)
    end_time = timeit.default_timer()
    print(f"Birthdays calculated: {len(birthdays)}")
    print(f"Anniversaries calculated: {len(anniversaries)}")
    results = process_large_list(sample_start, sample_end)
    print(f"Processed large list efficiency score: {results}")