def evaluate_predicate(lists):
    return all(all(x % 2 == 0 for x in sublist) for sublist in lists)

if __name__ == '__main__':
    sample_lists = [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
    print(evaluate_predicate(sample_lists))