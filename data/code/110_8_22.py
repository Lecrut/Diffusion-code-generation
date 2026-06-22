from datetime import date

class ChronologicalSorter:
    SORT_METHOD = 'sort'
    
    @staticmethod
    def sort_dates(event_list):
        if not isinstance(event_list, list):
            raise ValueError("Input must be a list")
        dates_copy = list(event_list)
        dates_copy.sort()
        return dates_copy

if __name__ == '__main__':
    events = [
        date(2023, 12, 25),
        date(2021, 1, 1),
        date(2022, 7, 4),
        date(2020, 10, 31),
        date(2023, 1, 1)
    ]
    result = ChronologicalSorter.sort_dates(events)
    for d in result:
        print(d)