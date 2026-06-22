def calculate_length_ratio(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    
    if len_str2 == 0:
        return float('inf') if len_str1 != 0 else 1.0
    
    return len_str1 / len_str2

if __name__ == '__main__':
    sample_string1 = "Alibaba Cloud"
    sample_string2 = "Qwen AI Model"
    
    ratio_result = calculate_length_ratio(sample_string1, sample_string2)
    print(ratio_result)