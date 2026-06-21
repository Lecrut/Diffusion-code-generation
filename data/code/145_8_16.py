def evaluate_predicate(lst):
    if len(lst) < 2:
        return False
    for i in range(len(lst) - 1):
        if lst[i] >= lst[i + 1]:
            return False
    return True

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(evaluate_predicate(sample_list))