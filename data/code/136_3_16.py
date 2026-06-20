def filter_tuples(tuples, criteria):
    if not tuples or not criteria:
        return []
    filtered = [t for t in tuples if all((c(t) for c in criteria))]
    return filtered
if __name__ == '__main__':
    sample_tuples = [(1, 2), (3, 4), (5, 6)]
    even_first_element = lambda x: x[0] % 2 == 0
    greater_than_five = lambda x: x[1] > 5
    criteria = [even_first_element, greater_than_five]
    result = filter_tuples(sample_tuples, criteria)
    print(result)