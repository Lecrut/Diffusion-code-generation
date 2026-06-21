from datetime import datetime
from typing import List

class DateSorter:
    FORMAT_STR = '%Y-%m-%d'

    @staticmethod
    def _parse(date_str: str) -> datetime:
        return datetime.strptime(date_str, DateSorter.FORMAT_STR)

    @staticmethod
    def sort(date_strings: List[str]) -> List[str]:
        if not date_strings:
            return []
        validated = []
        for d in date_strings:
            parsed = DateSorter._parse(d)
            validated.append((d, parsed))
        validated.sort(key=lambda x: x[1])
        return [item[0] for item in validated]

if __name__ == '__main__':
    sample_dates = ['2023-10-01', '2021-05-15', '2022-01-01', '2023-01-01']
    sorted_list = DateSorter.sort(sample_dates)
    print(sorted_list)