def extract_max_integer(str_list):
    return max(int(num) for num in str_list)

if __name__ == '__main__':
    sample_values = ["3", "5", "1", "20"]
    print(extract_max_integer(sample_values))