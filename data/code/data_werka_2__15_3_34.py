def compare_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError('Both inputs must be strings')
    return str1.lower() == str2.lower()
if __name__ == '__main__':
    sample_str1 = 'Alibaba'
    sample_str2 = 'alibaba'
    result = compare_strings(sample_str1, sample_str2)
    print(result)
    sample_str3 = 'Cloud'
    sample_str4 = 'cloudy'
    result = compare_strings(sample_str3, sample_str4)
    print(result)