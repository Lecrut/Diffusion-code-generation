def evaluate_predicate(lst, predicate):
    return any(predicate(x) for x in lst)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    predicate = lambda x: x % 2 == 0
    print(evaluate_predicate(sample_list, predicate))