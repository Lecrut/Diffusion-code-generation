from datetime import datetime, timezone
from typing import List

def sort_iso_dates(date_strings: List[str]) -> List[str]:
    if not date_strings:
        return []
    
    def parse_date(d: str) -> datetime:
        try:
            if d.endswith('Z'):
                d_clean = d[:-1] + '+00:00'
            else:
                d_clean = d
            return datetime.fromisoformat(d_clean)
        except ValueError:
            raise ValueError(f"Invalid ISO 8601 date string: {d}")
    
    parsed_with_original = [(parse_date(d), d) for d in date_strings]
    parsed_with_original.sort(key=lambda x: x[0])
    
    return [d for _, d in parsed_with_original]

if __name__ == '__main__':
    sample_dates = [
        "2024-06-15T10:00:00Z",
        "2023-11-20T14:30:00+02:00",
        "2025-01-01T00:00:00",
        "2022-08-10T18:45:00-05:00",
        "2024-06-15T10:00:00+00:00"
    ]
    
    sorted_result = sort_iso_dates(sample_dates)
    print(sorted_result)