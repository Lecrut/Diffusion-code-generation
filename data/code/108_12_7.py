from datetime import datetime

class DateParser:
    def parse_day_from_iso(self, iso_date: str) -> int:
        try:
            date_obj = datetime.fromisoformat(iso_date)
            return date_obj.day
        except ValueError:
            raise ValueError("Invalid ISO date format. Please use YYYY-MM-DDTHH:mm:ss")

if __name__ == '__main__':
    parser = DateParser()
    sample_iso_date = "2024-07-04T12:00:00"
    print(f"Day from '{sample_iso_date}': {parser.parse_day_from_iso(sample_iso_date)}")