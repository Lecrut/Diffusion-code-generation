def clean_and_convert(lst):
    cleaned_list = []
    for item in lst:
        if isinstance(item, (int, float)):
            cleaned_list.append(item)
        elif isinstance(item, str) and item.replace('.', '', 1).isdigit():
            cleaned_list.append(int(item) if '.' not in item else float(item))
    return cleaned_list

if __name__ == '__main__':
    sample_values = [1, '2', 3.0, None, '4.5', 'abc']
    print(clean_and_convert(sample_values))