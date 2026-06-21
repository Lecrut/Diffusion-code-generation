def evaluate_predicate(predicate, data):
    return predicate(data)

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    sample_predicate = lambda x: any(i % 2 == 0 for i in x)
    print(evaluate_predicate(sample_predicate, sample_data))