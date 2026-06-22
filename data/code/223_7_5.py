def extract_max_integer(string_list):
    return max(map(int, string_list))

if __name__ == '__main__':
    sample_values = ["3", "54", "23", "98"]
    print(extract_max_integer(sample_values))