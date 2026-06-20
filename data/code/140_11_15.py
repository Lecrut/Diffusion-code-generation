NUMERIC_TYPES = (int, float)
STRING_NUMERIC_REGEX = r'^-?\d+(\.\d+)?$'

def clean_and_convert(data):
    cleaned_data = []
    for item in data:
        if isinstance(item, NUMERIC_TYPES):
            cleaned_data.append(item)
        elif isinstance(item, str) and re.match(STRING_NUMERIC_REGEX, item):
            cleaned_data.append(int(item) if '.' not in item else float(item))
    return cleaned_data

if __name__ == '__main__':
    sample_data = [1, '2', 3.0, None, '4.5', 'abc']
    print(clean_and_convert(sample_data))