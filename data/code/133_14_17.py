def evaluate_tf_statements(assrt_list):
    return {assrt: eval(assrt) for assrt in assrt_list}

if __name__ == '__main__':
    sample_values = ["True", "False", "2 + 2 == 4", "3 > 5"]
    print(evaluate_tf_statements(sample_values))