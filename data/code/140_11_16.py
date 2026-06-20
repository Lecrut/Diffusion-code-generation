def clean_and_convert(data: list) -> list:
    cleaned_data = []
    for item in data:
        if isinstance(item, (int, float)):
            cleaned_data.append(item)
        elif isinstance(item, str):
            try:
                num = float(item)
                if num.is_integer():
                    cleaned_data.append(int(num))
                else:
                    cleaned_data.append(num)
            except ValueError:
                continue
    return cleaned_data

if __name__ == '__main__':
    sample_data = [1, '2', 3.0, None, '4.5', 'abc', '7.8']
    print(clean_and_convert(sample_data))