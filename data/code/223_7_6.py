def extract_max_integer(string_list):
    return max(int(num) for num in string_list)

if __name__ == '__main__':
    sample_values = ["3", "45", "12", "90"]
    print(extract_max_integer(sample_values))