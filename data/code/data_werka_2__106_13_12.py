import time

YEARS_MAP = {
    0: 0,
    1: 31536000,
    2: 63072000,
    3: 94608000,
    4: 126144000,
    5: 157680000,
    6: 189216000,
    7: 220752000,
    8: 252288000,
    9: 283824000,
    10: 315360000
}

def calculate_year_difference(timestamp1: int, timestamp2: int) -> int:
    if timestamp1 < 0 or timestamp2 < 0:
        raise ValueError("Timestamps must be non-negative")
    
    if timestamp1 == timestamp2:
        return 0
    
    diff = abs(timestamp1 - timestamp2)
    
    if diff < 31536000:
        return 0
    
    years = 0
    for val in YEARS_MAP.values():
        if diff >= val:
            years = val // 31536000
        else:
            break
            
    return years

if __name__ == '__main__':
    ts1 = 1609459200
    ts2 = 1640995200
    result = calculate_year_difference(ts1, ts2)
    print(result)