class DateComparator:
    def __init__(self, date_string_1: str, date_string_2: str):
        self.date_string_1 = date_string_1
        self.date_string_2 = date_string_2
        self.parsed_1 = self._parse_date(date_string_1)
        self.parsed_2 = self._parse_date(date_string_2)

    def _parse_date(self, date_str: str):
        components = date_str.split('-')
        if len(components) != 3:
            raise ValueError("Invalid date format")
        return (int(components[0]), int(components[1]), int(components[2]))

    def is_date_1_later(self):
        if self.parsed_1 > self.parsed_2:
            return True
        return False

    def is_date_2_later(self):
        if self.parsed_2 > self.parsed_1:
            return True
        return False

    def get_later_date(self):
        if self.parsed_1 > self.parsed_2:
            return self.date_string_1
        if self.parsed_2 > self.parsed_1:
            return self.date_string_2
        return self.date_string_1

if __name__ == '__main__':
    comparator = DateComparator("2023-02-28", "2023-03-01")
    print(comparator.get_later_date())
    print(comparator.is_date_1_later())
    print(comparator.is_date_2_later())