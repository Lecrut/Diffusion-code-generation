MAX_NUM = 100

def extract_max_integer(str_list):
    return max(int(num) for num in str_list if int(num) <= MAX_NUM)

if __name__ == '__main__':
    sample_values = ["3", "56", "23", "89"]
    print(extract_max_integer(sample_values))