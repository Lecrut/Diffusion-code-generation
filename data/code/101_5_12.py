import time

class DateAnalyzer:
    WEEKDAY_MAP = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }

    @staticmethod
    def _parse_date_to_timestamp(date_str):
        struct_time = time.strptime(date_str, "%Y-%m-%d")
        return time.mktime(struct_time)

    @staticmethod
    def _get_weekday_index_from_timestamp(timestamp):
        local_time = time.localtime(timestamp)
        return local_time.tm_wday

    def get_weekday_name(self, date_str):
        timestamp = self._parse_date_to_timestamp(date_str)
        index = self._get_weekday_index_from_timestamp(timestamp)
        return self.WEEKDAY_MAP[index]

if __name__ == '__main__':
    analyzer = DateAnalyzer()
    target_date = '2023-01-01'
    weekday_name = analyzer.get_weekday_name(target_date)
    print(weekday_name)