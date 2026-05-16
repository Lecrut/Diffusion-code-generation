def evaluate_strings(input_list):
    for s in input_list:
        yield s.lower() in ('true', '1', 'yes')
if __name__ == '__main__':
    sample_list = ["True", "False", "1", "No", "Yes", "0"]
    results_generator = evaluate_strings(sample_list)
    results_list = list(results_generator)
    print(results_list)