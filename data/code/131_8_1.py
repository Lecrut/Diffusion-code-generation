import bisect
def decide_based_on_rules(data, rules):
    if not rules:
        return None
    sorted_thresholds = [rule[0] for rule in rules]
    def find_index(value):
        return bisect.bisect_right(sorted_thresholds, value)
    if not sorted_thresholds:
        return None
    idx = find_index(data)
    if idx == 0:
        return rules[0][1]
    elif idx < len(sorted_thresholds):
        return rules[idx - 1][1]
    else:
        return rules[-1][1]
if __name__ == '__main__':
    data_points = [10, 25, 40, 55, 70, 85, 100]
    decision_rules = [
        (20, 'Low'),
        (50, 'Medium'),
        (80, 'High')
    ]
    print(f"Data Points: {data_points}")
    print(f"Rules: {decision_rules}")
    for data in data_points:
        result = decide_based_on_rules(data, decision_rules)
        print(f"Input: {data}, Decision: {result}")