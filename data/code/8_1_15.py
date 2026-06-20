import re

def split_csv_string(csv_string):
    if not csv_string:
        return []
    parts = re.split(r',', csv_string)
    result = []
    for part in parts:
        if part:
            result.append(part)
    return result

if __name__ == '__main__':
    sample_csv = "a,,b, c, ,d"
    output = split_csv_string(sample_csv)
    print(output)