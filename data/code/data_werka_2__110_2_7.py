import datetime
import time

class ISODateSorter:
    def __init__(self, date_strings):
        self.date_strings = list(date_strings)
        self.parsed_data = []
        self._parse_all()

    def _parse_all(self):
        for date_str in self.date_strings:
            try:
                dt = datetime.datetime.fromisoformat(date_str)
                ts = dt.timestamp()
                self.parsed_data.append((ts, date_str))
            except (ValueError, TypeError) as e:
                raise ValueError(f"Invalid date format: {date_str}") from e

    def sort_ascending(self):
        self.parsed_data.sort(key=lambda x: x[0])
        return [item[1] for item in self.parsed_data]

    def sort_descending(self):
        self.parsed_data.sort(key=lambda x: x[0], reverse=True)
        return [item[1] for item in self.parsed_data]

    def get_timestamps(self):
        return [item[0] for item in self.parsed_data]

if __name__ == '__main__':
    sample_dates = [
        "2023-10-01T12:00:00",
        "2021-05-15T08:30:00",
        "2023-01-20T18:45:00",
        "2022-12-31T23:59:59",
        "2020-02-29T00:00:00"
    ]
    sorter = ISODateSorter(sample_dates)
    ascending_result = sorter.sort_ascending()
    descending_result = sorter.sort_descending()
    timestamps = sorter.get_timestamps()
    print(ascending_result)
    print(descending_result)
    print(timestamps)