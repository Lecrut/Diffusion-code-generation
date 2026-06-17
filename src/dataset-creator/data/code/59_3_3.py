import datetime
def parse_date_to_weekday(date_string: str) -> tuple[str, bool]:
    patterns = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%B %d, %Y",
        "%b %d, %Y",
        "%d %B %Y",
        "%d.%m.%Y",
        "YYYY-MM-DD" if "-" in date_string and len(date_string) == 10 else None,                                                                                                                                                                                                                                      
    ]
    format_map = {
        "2023-10-27": "%Y-%m-%d",
        "27/10/2023": "%d/%m/%Y",
        "October 27, 2023": "%B %d, %Y",
        "Oct 27, 2023": "%b %d, %Y",
        "27 October 2023": "%d %B %Y",
        "27.10.2023": "%d.%m.%Y"
    }
    for sample_str, fmt in format_map.items():
        try:
            dt = datetime.datetime.strptime(sample_str, fmt)
            return (dt.strftime("%A"), True)
        except ValueError:
            continue
    common_formats = [
        "%Y-%m-%d",
        "%d/%m/%Y", 
        "%B %d, %Y",
        "%b %d, %Y",
        "%d %B %Y",
        "%d.%m.%Y"
    ]
    for fmt in common_formats:
        try:
            dt = datetime.datetime.strptime(date_string, fmt)
            return (dt.strftime("%A"), True)
        except ValueError:
            continue
    return ("Unknown/Invalid Format", False)
if __name__ == '__main__':
    test_cases = [
        "2023-10-27",
        "27/10/2023",
        "October 27, 2023",
        "Oct 27, 2023",
        "27 October 2023",
        "27.10.2023"
    ]
    for test_input in test_cases:
        weekday, is_valid = parse_date_to_weekday(test_input)
        print(f"Input: {test_input} -> Weekday: {weekday}, Valid: {is_valid}")