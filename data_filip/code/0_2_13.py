import re

def extract_digits_to_tuple(s):
    digits = re.findall(r'\d', s)
    return tuple(int(d) for d in digits)

if __name__ == '__main__':
    sample_string = "Room 305, Floor 12, Code X-77, Year 2023"
    result = extract_digits_to_tuple(sample_string)
    print(result)