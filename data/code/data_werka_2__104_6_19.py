class DateComparator:
    FORMAT = "%Y-%m-%d"

    @staticmethod
    def _parse(date_string: str):
        from datetime import datetime
        return datetime.strptime(date_string, DateComparator.FORMAT)

    def compare(self, date_a: str, date_b: str) -> str:
        dt_a = self._parse(date_a)
        dt_b = self._parse(date_b)
        if dt_a < dt_b:
            return "date_a is earlier"
        if dt_a > dt_b:
            return "date_b is earlier"
        return "dates are equal"

if __name__ == '__main__':
    comparator = DateComparator()
    output = comparator.compare("2024-12-31", "2024-01-01")
    print(output)