from datetime import datetime

class ChronologicalSorter:
    def __init__(self, items):
        self.items = list(items)

    def sort(self):
        return sorted(self.items)

    def get_unsorted(self):
        return list(self.items)

if __name__ == '__main__':
    dt_a = datetime(2024, 1, 1, 10, 0)
    dt_b = datetime(2023, 12, 31, 23, 59)
    dt_c = datetime(2024, 2, 1, 0, 0)
    dt_d = datetime(2023, 12, 31, 23, 59, 1)

    original_data = [dt_a, dt_b, dt_c, dt_d]
    sorter = ChronologicalSorter(original_data)

    unsorted_check = sorter.get_unsorted()
    print(unsorted_check)

    sorted_data = sorter.sort()
    print(sorted_data)