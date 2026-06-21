from datetime import date

class ChronologicalSorter:
    def __init__(self, events):
        self.events = events

    def get_sorted(self):
        if not self.events:
            return []
        self.events.sort()
        return self.events

def format_events(dates):
    return [str(d) for d in dates]

if __name__ == '__main__':
    raw_dates = [
        date(1999, 12, 31),
        date(2020, 1, 1),
        date(2005, 8, 15),
        date(2020, 1, 1),
        date(1980, 5, 5)
    ]
    sorter = ChronologicalSorter(raw_dates)
    sorted_list = sorter.get_sorted()
    formatted = format_events(sorted_list)
    for entry in formatted:
        print(entry)