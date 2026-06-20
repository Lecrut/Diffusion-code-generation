def clean_and_convert(lst):
    cleaned_list = []
    for item in lst:
        if isinstance(item, (int, float)):
            cleaned_list.append(item)
        elif isinstance(item, str) and item.replace('.', '', 1).isdigit():
            if '.' in item:
                cleaned_list.append(float(item))
            else:
                cleaned_list.append(int(item))
    return cleaned_list

if __name__ == '__main__':
    sample_values = [1, '2', 3.0, '4.5', None, 'abc']
    print(clean_and_convert(sample_values))