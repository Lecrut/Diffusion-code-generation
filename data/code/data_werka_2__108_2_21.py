import time

class DateExtractor:
    DAY_FIELD = 3

    @staticmethod
    def _get_structured_time():
        return time.localtime()

    def get_current_day(self):
        structured = self._get_structured_time()
        return structured[self.DAY_FIELD]

if __name__ == '__main__':
    extractor = DateExtractor()
    day = extractor.get_current_day()
    print(day)