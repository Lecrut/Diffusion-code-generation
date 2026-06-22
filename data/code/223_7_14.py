def extract_max_integer(str_list):
    return max(int(num) for num in str_list)

if __name__ == '__main__':
    sample_values = ["10", "20", "30", "40"]
    result = extract_max_integer(sample_values)
    print(result)