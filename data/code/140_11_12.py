def clean_and_convert(lst):
    return [int(x) if isinstance(x, str) and x.isdigit() else float(x) for x in lst if isinstance(x, (int, float, str))]

if __name__ == '__main__':
    sample_list = [1, '2', 3.0, None, '4.5']
    cleaned_list = clean_and_convert(sample_list)
    print(cleaned_list)