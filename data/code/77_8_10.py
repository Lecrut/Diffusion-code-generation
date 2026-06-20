import re

def time_to_minutes(time_str):
    patterns = [
        (r'^(\d{1,2}):(\d{2})$', lambda m: int(m.group(1)) * 60 + int(m.group(2))),
        (r'^(\d{1,2})h(\d{1,2})m$', lambda m: int(m.group(1)) * 60 + int(m.group(2)))
    ]
    
    for pattern, func in patterns:
        match = re.match(pattern, time_str)
        if match:
            return func(match)
    
    raise ValueError("Invalid time format")

if __name__ == '__main__':
    print(time_to_minutes('10:30'))
    print(time_to_minutes('10h30m'))