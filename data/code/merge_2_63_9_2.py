from datetime import datetime
import pytz
def subtract_years(date: datetime, years: int) -> datetime:
    return date.replace(year=date.year - abs(years)) if years > 0 else date.replace(year=date.year + abs(years))
if __name__ == '__main__':
    base_date = datetime(2023, 6, 15, 14, 30)
    tz_info = pytz.timezone('US/Eastern')
    localized_date = tz_info.localize(base_date.replace(tzinfo=None))
    result_older = subtract_years(localized_date, 5)
    result_newer = subtract_years(localized_date, -2)
    print(f"Original: {localized_date}")
    print(f"Mined by 5 years: {result_older}")
    print("Minued by 2 years: {result_newer}".format(result_newer=result_newer))