def evaluate_strings(string_list):
    for s in string_list:
        yield s.lower() in ('true', '1', 'yes')
if __name__ == '__main__':
    input_list = ["True", "False", "1", "No", "Yes", "0"]
    results = evaluate_strings(input_list)
    output_list = list(results)
    print(output_list)