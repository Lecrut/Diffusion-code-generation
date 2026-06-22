class DateSorter:
    MONTH_NAMES = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }

    def __init__(self, dates):
        self.dates = dates

    def sort_chronologically(self):
        return sorted(self.dates)

    def format_date(self, date_tuple):
        y, m, d = date_tuple
        month_name = self.MONTH_NAMES.get(m, "Unknown")
        return f"{month_name} {d}, {y}"

if __name__ == '__main__':
    raw_dates = [
        (2024, 12, 25),
        (2023, 3, 14),
        (2024, 1, 1),
        (2022, 7, 4),
        (2023, 11, 23)
    ]
    sorter = DateSorter(raw_dates)
    sorted_results = sorter.sort_chronologically()
    print(sorted_results)
    print(sorter.format_date(sorted_results[0]))