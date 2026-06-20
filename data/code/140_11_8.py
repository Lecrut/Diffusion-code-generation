NUMERIC_TYPES = (int, float)

def clean_and_convert(data):
    cleaned_data = []
    for item in data:
        if isinstance(item, NUMERIC_TYPES) or (isinstance(item, str) and item.replace('.', '', 1).isdigit()):
            value = int(item) if '.' not in item else float(item)
            cleaned_data.append(value)
    return cleaned_data

if __name__ == '__main__':
    sample_data = [1, '2', 3.0, None, '4.5', 'abc']
    print(clean_and_convert(sample_data))