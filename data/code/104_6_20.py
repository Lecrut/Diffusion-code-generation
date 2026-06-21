from datetime import datetime

DATE_FORMAT: str = "%Y-%m-%d"
RESULT_EARLIER: str = "earlier"
RESULT_LATER: str = "later"
RESULT_EQUAL: str = "equal"

def compare_dates(date_str1: str, date_str2: str) -> str:
    dt1: datetime = datetime.strptime(date_str1, DATE_FORMAT)
    dt2: datetime = datetime.strptime(date_str2, DATE_FORMAT)
    if dt1 < dt2:
        return RESULT_EARLIER
    if dt1 > dt2:
        return RESULT_LATER
    return RESULT_EQUAL

if __name__ == '__main__':
    result: str = compare_dates("2024-05-10", "2024-05-10")
    print(result)