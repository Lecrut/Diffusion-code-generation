def evaluate_predicate(predicate, values):
    return predicate(values)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    sample_predicate = lambda x: all(i % 2 != 0 for i in x)
    print(evaluate_predicate(sample_predicate, sample_values))