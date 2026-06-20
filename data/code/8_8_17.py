import re

def split_and_clean(csv_string):
    if not csv_string:
        return []
    parts = csv_string.split(',')
    return [part.strip() for part in parts if part.strip()]

if __name__ == '__main__':
    sample = " hello , world , , test , , "
    result = split_and_clean(sample)
    print(result)