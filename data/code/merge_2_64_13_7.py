import datetime as dt
def parse_date_to_full_month(date_str: str) -> str:
    pattern_map = {
        'dd/mm/yyyy': r'(\d{2})/(\d{2})/(\d{4})',
        'mm/dd/yyyy': r'(\d{2}/\d{2})/(\\d{4})',                                                                                                                                                                                                                                                      
        'yyyy-mm-dd': r'(\\d{4})-(\\d{2})-(\\d{2})',
    }
    import re
    match = re.search(r'(\\d{4})-(\\d{2})-(\\d{2})', date_str)
    if match:
        year, month, day = int(match.group(1)), int(match.group(2)), int(match.group(3))
        return dt.date(year=year, month=month, day=day).strftime('%B')
    match = re.search(r'(\\d{2})/(\\d{2})/(\\d{4})', date_str)
    if match:
        try:
            year, month, day = int(match.group(3)), int(match.group(2)), int(match.group(1))
            return dt.date(year=year, month=month, day=day).strftime('%B')
        except ValueError:
            pass
    match = re.search(r'(\\d{2})/(\\d{2})/(\\d{4})', date_str)
    if match:
        try:
            month, day, year = int(match.group(1)), int(match.group(2)), int(match.group(3))
            return dt.date(year=year, month=month, day=day).strftime('%B')
        except ValueError:
            pass
    match = re.search(r'(\\d{4})/(\\d{2})/(\\d{2})', date_str)
    if match:
        try:
            year, month, day = int(match.group(1)), int(match.group(2)), int(match.group(3))
            return dt.date(year=year, month=month, day=day).strftime('%B')
        except ValueError:
            pass
    return "Unknown"
if __name__ == '__main__':
    sample_dates = [
        '25/12/2023',                                             
        '12/25/2023',                                                                                                                                                
        '25/12/2023',                              
        '12/24/2023',                                                                                      
    ]
    sample_dates = [
        '25/12/2023',                              
        '12/24/2023',                                                                                    
    ]
    sample_dates = [
        '25/12/2023',                               
        '01/24/2023',                                             
        '2023-06-15',                               
    ]
    results = []
    for date_str in sample_dates:
        try:
            result = parse_date_to_full_month(date_str)
            results.append(f"{date_str} => {result}")
        except Exception as e:
            results.append(f"Error parsing '{date_str}': {e}")
    print('\n'.join(results))