def process_strings(string_list):
    processed_list = []
    for s in string_list:
        processed_list.append(s.replace(' ', ''))
    return processed_list
if __name__ == '__main__':
    sample_input = ["hello world", "  a b c ", "single", "multiple spaces here"]
    result = process_strings(sample_input)
    print(result)