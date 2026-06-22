from datetime import datetime
from typing import List

def sort_dates(date_strings: List[str]) -> List[str]:
    def parse_date(date_str: str) -> datetime:
        try:
            return datetime.strptime(date_str, '%d/%m/%Y')
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}") from e

    return sorted(date_strings, key=parse_date)

if __name__ == '__main__':
    sample_dates = ['25/12/2023', '01/01/2024', '15/06/2023', '31/12/2022']
    sorted_dates = sort_dates(sample_dates)
    print(sorted_dates)