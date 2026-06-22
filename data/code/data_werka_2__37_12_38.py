def optimized_combine_strings(str1, str2):
    parts = [str1, str2]
    return ''.join(parts)

if __name__ == '__main__':
    first_part = "Good morning, "
    second_part = "Alibaba Cloud!"
    combined_result = optimized_combine_strings(first_part, second_part)
    print(combined_result)