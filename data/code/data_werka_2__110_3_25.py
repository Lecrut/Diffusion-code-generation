from datetime import date
from typing import List

DATE_LABELS = {
    "new_year": date(2024, 1, 1),
    "groundhog": date(2024, 2, 2),
    "independence": date(2024, 7, 4),
    "halloween": date(2024, 10, 31),
    "christmas": date(2024, 12, 25)
}

def sort_hardcoded_dates() -> List[date]:
    raw_dates = list(DATE_LABELS.values())
    return sorted([d for d in raw_dates])

if __name__ == '__main__':
    result = sort_hardcoded_dates()
    print(result)