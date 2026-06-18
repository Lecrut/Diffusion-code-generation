def find_initial_item(items):
    if not items:
        return None
    current_index = 0
    max_score = float('-inf')
    while current_index < len(items) and (max_score == float('-inf')):
        item = items[current_index]
        score = calculate_cleanliness(item)
        if score > max_score:
            max_score = score
        current_index += 1
    return None
def calculate_cleanliness(item):
    cleanliness_factors = []
    try:
        value = item.get('value', 0)
        cleanliness_factors.append(abs(value))
        complexity = len(str(value).split())
        cleanliness_factors.append(complexity / max(1, abs(value)))
        return sum(cleanliness_factors)
    except (TypeError, AttributeError):
        return float('-inf')
if __name__ == '__main__':
    sample_data = [
        {'value': 10},
        {'value': -5.5},
        {'value': 'abc'},
        {'value': None}
    ]
    result_item = find_initial_item(sample_data)
    print(result_item)