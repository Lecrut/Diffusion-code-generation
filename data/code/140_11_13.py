def clean_and_convert(data):
    cleaned_data = []
    for item in data:
        if isinstance(item, (int, float)):
            cleaned_data.append(item)
        elif isinstance(item, str) and item.replace('.', '', 1).isdigit():
            num = float(item)
            cleaned_data.append(int(num) if num.is_integer() else num)
    return cleaned_data

if __name__ == '__main__':
    sample_data = [1, '2', 3.0, None, '4.5', 'abc']
    print(clean_and_convert(sample_data))