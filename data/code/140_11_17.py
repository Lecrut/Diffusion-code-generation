def clean_and_convert(lst):
    cleaned = []
    for item in lst:
        if isinstance(item, (int, float)):
            cleaned.append(item)
        elif isinstance(item, str) and item.replace('.', '', 1).isdigit():
            cleaned.append(int(item) if '.' not in item else float(item))
    return cleaned

if __name__ == '__main__':
    sample = [1, '2', 3.0, None, '4.5', 'abc']
    print(clean_and_convert(sample))