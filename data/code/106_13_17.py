import struct

def calculate_year_difference(timestamp1: int, timestamp2: int) -> int:
    if not isinstance(timestamp1, (int, float)):
        raise ValueError("timestamp1 must be an integer or float")
    if not isinstance(timestamp2, (int, float)):
        raise ValueError("timestamp2 must be an integer or float")
    
    epoch_offset = 2208988800
    years_since_1900 = 70
    
    if timestamp1 > 0 and timestamp2 > 0:
        val1 = timestamp1 + epoch_offset
        val2 = timestamp2 + epoch_offset
        
        packed1 = struct.pack('>I', int(val1) & 0xFFFFFFFF)
        packed2 = struct.pack('>I', int(val2) & 0xFFFFFFFF)
        
        year1 = struct.unpack('>H', packed1[0:2])[0]
        year2 = struct.unpack('>H', packed2[0:2])[0]
        
        actual_year1 = year1 + years_since_1900
        actual_year2 = year2 + years_since_1900
        
        return abs(actual_year1 - actual_year2)
    elif timestamp1 == 0 and timestamp2 == 0:
        return 0
    else:
        raise ValueError("Timestamps must be positive")

if __name__ == '__main__':
    ts1 = 1609459200
    ts2 = 1640995200
    result = calculate_year_difference(ts1, ts2)
    print(result)