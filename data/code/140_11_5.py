def clean_and_convert(data):
    cleaned_data = []
    for item in data:
        if isinstance(item, (int, float)):
            cleaned_data.append(item)
        elif isinstance(item, str):
            try:
                if '.' not in item:
                    cleaned_data.append(int(item))
                else:
                    cleaned_data.append(float(item))
            except ValueError:
                continue
    return cleaned_data

if __name__ == '__main__':
    sample_data = [1, '2', 3.0, None, '4.5', 'abc']
    print(clean_and_convert(sample_data))