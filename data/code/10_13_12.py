def get_head(input_list):
    if not input_list:
        return None
    return input_list[0]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_head(sample_list)
    print(result)