import bisect
def decide_based_on_rules(data, rules):
    if not rules:
        return None
    thresholds = [rule[0] for rule in rules]
    def find_index(value):
        if not thresholds:
            return -1
        idx = bisect.bisect_right(thresholds, value)
        if idx == 0:
            return 0
        return idx - 1
    if not data:
        return None
    sorted_thresholds = sorted(list(set(thresholds)))
    def lookup(value):
        if not sorted_thresholds:
            return None
        idx = bisect.bisect_right(sorted_thresholds, value)
        if idx == 0:
            return rules[0][1]
        return rules[idx - 1][1]
    results = []
    for item in data:
        results.append(lookup(item))
    return results
if __name__ == '__main__':
    sample_data = [10, 25, 5, 30, 15]
    sample_rules = [(10, 'Low'), (20, 'Medium'), (35, 'High')]
    result = decide_based_on_rules(sample_data, sample_rules)
    print(result)