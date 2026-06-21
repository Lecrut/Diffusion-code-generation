def evaluate_predicate(predicate, data):
    return predicate(data)

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    sample_predicate = lambda x: any(y % 2 == 0 for y in x)
    print(evaluate_predicate(sample_predicate, sample_data))