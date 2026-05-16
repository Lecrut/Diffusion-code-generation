def analyze_list(input_list):
    list_name = "input_list"
    list_length = len(input_list)
    result_dict = {list_name: list_length}
    return result_dict
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    analysis = analyze_list(sample_list)
    print(analysis)