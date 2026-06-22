import re

def filter_empty_csv_segments(csv_string: str) -> list:
    if not csv_string:
        return []
    
    parts = csv_string.split(',')
    result = []
    
    for part in parts:
        if part:
            result.append(part)
            
    return result

if __name__ == '__main__':
    sample_csv = "apple,,banana,,cherry,"
    result = filter_empty_csv_segments(sample_csv)
    print(result)