import datetime
def parse_and_get_weekday(date_str: str) -> tuple[str, bool]:
    formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%B %d, %Y",
        "%y/%m/%d",
        "dd.mm.yyyy"
    ]
    for fmt in formats:
        try:
            parsed_date = datetime.datetime.strptime(date_str, fmt)
            return (parsed_date.strftime("%A"), True)
        except ValueError:
            continue
    return ("Unknown format", False)
if __name__ == '__main__':
    samples = [
        "2023-10-05",
        "05/10/2023",
        "October 05, 2023",
        "23/10/05",
        "05.10.2023"
    ]
    for sample in samples:
        weekday, is_valid = parse_and_get_weekday(sample)
        print(f"{sample} -> {weekday}, Validated: {is_valid}")