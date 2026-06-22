def split_and_filter(s):
    parts = s.split(',')
    result = list(filter(lambda x: x.strip(), parts))
    return result

if __name__ == '__main__':
    sample_input = "apple, , banana, , ,cherry, "
    filtered_result = split_and_filter(sample_input)
    print(filtered_result)