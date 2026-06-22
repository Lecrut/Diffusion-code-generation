class DateComparator:
    YEAR_INDEX = slice(0, 4)
    MONTH_INDEX = slice(5, 7)
    DAY_INDEX = slice(8, 10)
    SEPARATOR = '-'

    @staticmethod
    def _parse(date_str):
        if len(date_str) < 10:
            raise ValueError("Invalid date format")
        year = int(date_str[DateComparator.YEAR_INDEX])
        month = int(date_str[DateComparator.MONTH_INDEX])
        day = int(date_str[DateComparator.DAY_INDEX])
        return (year, month, day)

    def compare(self, date1, date2):
        d1 = self._parse(date1)
        d2 = self._parse(date2)
        if d1 > d2:
            return date1
        elif d2 > d1:
            return date2
        return date1

if __name__ == '__main__':
    comp = DateComparator()
    result = comp.compare("2020-02-29", "2021-02-28")
    print(result)