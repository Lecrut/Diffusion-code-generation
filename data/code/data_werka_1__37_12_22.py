def optimized_combine(str1, str2):
    return ''.join([str1, str2])

if __name__ == '__main__':
    sample_str1 = "Hello, "
    sample_str2 = "World!"
    combined_result = optimized_combine(sample_str1, sample_str2)
    print(combined_result)