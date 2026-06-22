from datetime import datetime

class DateSorter:
    FORMAT = '%Y-%m-%d'

    @staticmethod
    def _convert(date_str: str) -> datetime:
        return datetime.strptime(date_str, DateSorter.FORMAT)

    @staticmethod
    def sort(date_list: list) -> list:
        return sorted(date_list, key=DateSorter._convert)

if __name__ == '__main__':
    unsorted = ['2024-02-15', '2023-12-25', '2025-01-01', '2023-12-25']
    sorted_result = DateSorter.sort(unsorted)
    print(sorted_result)