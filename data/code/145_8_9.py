def evaluate_predicate(predicate, *lists):
    def short_circuit_eval(pred, lst):
        for item in lst:
            if pred(item):
                return True
        return False

    return all(short_circuit_eval(pred, lst) for pred, lst in zip(predicate, lists))

if __name__ == '__main__':
    predicate = [lambda x: x % 2 == 0, lambda x: x > 10]
    lists = [[2, 4, 6], [15, 20, 25]]
    print(evaluate_predicate(predicate, *lists))