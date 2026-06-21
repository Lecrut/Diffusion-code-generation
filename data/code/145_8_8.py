def evaluate_predicate(predicate):
    return predicate()

if __name__ == '__main__':
    def sample_predicate():
        a = [1, 2, 3]
        b = [4, 5, 6]
        return all(x < y for x in a for y in b)

    print(evaluate_predicate(sample_predicate))