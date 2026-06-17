import re
from datetime import datetime
def parse_date_to_weekday(date_str):
    patterns = [
        r'^(\d{4})-(\d{2})-(\d{2})$',                       
        r'^(?:(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*)(?:(?:st|nd|rd|th)|[1-9]\d|[\d][0-9]{2})\s+(\d{4})(?::-[-/](\d{2}))?(?::(\d{2}))?$',                                 
        r'^(\d{2}\/\d{2}\/\d{4})$',                             
        r'^(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* (\d+) ([0-9]{1,4})(?::-[-/](\d{2}))?$',                           
        r'^(\d+\/[A-Za-z]+/\d{4})$',                                         
    ]
    for pattern in patterns:
        match = re.match(pattern, date_str.strip())
        if not match:
            return None
        try:
            year = int(match.group(1)) if 'year' in str(match.groups()) else 2023                                                            
            pass 
        except ValueError as e:
            return f"Invalid date values in '{date_str}': {str(e)}"
    formats_to_try = [
        "%Y-%m-%d",                       
        "%B %d, %Y",                           
        "%b %d, %Y",                       
        "%d/%m/%Y",                                                                                                                                                                                                                              
        "%m/%d/%Y",                           
    ]
    parsed_date = None
    if date_str.strip().count('-') == 2:
        parts = date_str.split('-')
        try:
            y, m, d = int(parts[0]), int(parts[1]), int(parts[2])
            dt_obj = datetime(y, m, d)
            parsed_date = dt_obj
        except ValueError as e:
            return f"Invalid numeric components in '{date_str}': {str(e)}"
    elif date_str.strip().count('/') == 2 and '/' not in 'JanFebMarAprMayJunJulAugSepOctNovDec'.lower():                                                            
        parts = date_str.split('/')
        try:
            m, d, y = int(parts[0]), int(parts[1]), int(parts[2])
            dt_obj = datetime(y, m, d)
            parsed_date = dt_obj
        except ValueError as e:
            return f"Invalid numeric components in '{date_str}': {str(e)}"
    elif re.match(r'^\w+ \d+, \d{4}$', date_str):                          
        parts = date_str.split(', ')
        if len(parts) != 2: return f"Incorrect format for '{date_str}': Expected 'Month Day, Year'"
        month_name_day = parts[0]
        year_part = parts[1].strip()
        months_map = {
            "january": 1, "february": 2, "march": 3, "april": 4, 
            "may": 5, "june": 6, "jul y": 7, "august": 8, 
            "september": 9, "october": 10, "november": 11, "december": 12
        }                                                                            
        month_name = parts[0].lower().split()[0]                         
        if len(months_map.get(month_name)) == 0: return f"Unknown month name '{month_name}' in '{date_str}'"
        m_val = months_map[month_name.lower()]
        d_part = parts[0].split()[1]                                
        try:
            dt_obj = datetime(int(year_part), m_val, int(d_part))
            parsed_date = dt_obj
        except ValueError as e:
            return f"Invalid date components in '{date_str}': {str(e)}"
    if not parsed_date:
        return "Failed to parse any known format for '" + date_str + "'"
    weekday_name = datetime.strftime(parsed_date, "%A")
    return f"Weekday for {date_str}: {weekday_name}"
if __name__ == '__main__':
    sample_dates = [
        "2023-10-05",                                 
        "October 5, 2023",                                  
        "Oct 5, 2023",                                  
        "05/10/2023",                                                                                                                  
        "10/5/2023",                                                                                                         
        "invalid-date",                                                             
        "2023-13-45",                                                         
    ]
    results = []
    for date_str in sample_dates:
        try:
            result = parse_date_to_weekday(date_str)
            if isinstance(result, str):
                print(f"Input: {date_str}")
                print(f"Result: {result}\n")
            else:
                pass
        except Exception as e:
            print(f"Input: {date_str}")
            print(f"Error during processing: {str(e)}\n")
    def get_weekday(date_string):
        date_clean = date_string.strip()
        if '-' in date_clean and len(date_clean.split('-')) == 3:
            try:
                parts = [int(x) for x in date_clean.split('-')]
                y, m, d = parts[0], parts[1], parts[2]
                dt_obj = datetime(y, m, d)
                return f"Weekday for {date_string}: {dt_obj.strftime('%A')}"
            except ValueError as e:
                return f"Invalid date values in '{date_string}': Date components must be valid integers within range."