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
    idx = bisect.bisect_right(thresholds, data)
    if idx == 0:
        return rules[0][1]
    elif idx == len(thresholds):
        return rules[-1][1]
    else:
        return rules[idx - 1][1]
if __name__ == '__main__':
    sample_data = [10, 25, 5, 30, 15]
    sample_rules = [(5, 'Low'), (20, 'Medium'), (35, 'High')]
    print(f"Data: {sample_data}")
    print(f"Rules: {sample_rules}")
    results = []
    for item in sample_data:
        result = decide_based_on_rules(item, sample_rules)
        results.append((item, result))
    for data, result in results:
        print(f"Input {data}: Decision = {result}")