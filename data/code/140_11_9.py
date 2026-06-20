def clean_and_convert(data):
    cleaned_data = []
    for item in data:
        if isinstance(item, (int, float)):
            cleaned_data.append(item)
        elif isinstance(item, str) and '.' not in item and item.isdigit():
            cleaned_data.append(int(item))
        elif isinstance(item, str) and item.replace('.', '', 1).isdigit():
            cleaned_data.append(float(item))
    return cleaned_data

if __name__ == '__main__':
    sample_data = [1, '2', 3.0, None, '4.5', 'abc', '7.8']
    print(clean_and_convert(sample_data))