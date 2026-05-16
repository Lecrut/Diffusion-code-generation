def calculate_total_length(string_list):
    total_length = 0
    for s in string_list:
        total_length += len(s)
    return total_length
if __name__ == '__main__':
    sample_list = ["hello", "world", "python", "code"]
    result = calculate_total_length(sample_list)
    print(result)