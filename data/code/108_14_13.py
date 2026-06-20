class DateParser:
    @staticmethod
    def parse_date(date_string: str) -> int:
        year = int(date_string[:4])
        month = int(date_string[5:7])
        day = int(date_string[8:])
        return day

if __name__ == '__main__':
    parser = DateParser()
    sample_date_1 = "2023-10-27"
    sample_date_2 = "1999-01-01"
    sample_date_3 = "2024-02-29"
    print(f"Day of month for {sample_date_1}: {parser.parse_date(sample_date_1)}")
    print(f"Day of month for {sample_date_2}: {parser.parse_date(sample_date_2)}")
    print(f"Day of month for {sample_date_3}: {parser.parse_date(sample_date_3)}")