def compare_strings(str1, str2):
    def to_lowercase(s):
        return s.lower()
    
    lower_str1 = to_lowercase(str1)
    lower_str2 = to_lowercase(str2)
    
    return lower_str1 == lower_str2

if __name__ == '__main__':
    sample_string_1 = "Alibaba"
    sample_string_2 = "alibaba"
    result = compare_strings(sample_string_1, sample_string_2)
    print(result)