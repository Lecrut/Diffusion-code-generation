def evaluate_strings(input_list):
    for s in input_list:
        yield s.lower() in ('true', '1', 't')
if __name__ == '__main__':
    sample_list = ["True", "False", "1", "no", "t", "0"]
    results = evaluate_strings(sample_list)
    print(list(results))