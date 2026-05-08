def evaluate_strings(input_list):
    for s in input_list:
        yield s.lower() in ('true', '1', 't')
if __name__ == '__main__':
    sample_list = ["True", "False", "1", "no", "t"]
    results = evaluate_strings(sample_list)
    output_list = list(results)
    print(output_list)