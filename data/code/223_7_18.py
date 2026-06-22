def extract_max_integer(str_list):
    max_value = int(str_list[0])
    for s in str_list:
        num = int(s)
        if num > max_value:
            max_value = num
    return max_value

if __name__ == '__main__':
    sample_values = ["78", "123", "45", "90"]
    result = extract_max_integer(sample_values)
    print(result)