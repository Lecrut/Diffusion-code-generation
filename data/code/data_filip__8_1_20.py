import re

def split_csv_meaningful(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    parts = s.split(',')
    return [part for part in parts if part.strip()]

if __name__ == '__main__':
    sample_csv = "apple,,banana,  ,cherry,,"
    result = split_csv_meaningful(sample_csv)
    print(result)