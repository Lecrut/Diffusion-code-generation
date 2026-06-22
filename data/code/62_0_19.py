from collections import namedtuple

CategoryRecord = namedtuple('CategoryRecord', ['label', 'threshold'])

METRIC_CATEGORIES = {
    'low': CategoryRecord('low', 10),
    'mid': CategoryRecord('mid', 100),
    'high': CategoryRecord('high', 1000)
}

def compute_divisors(number):
    if number == 0:
        return []
    current = number
    if current < 0:
        current = -current
    found = set()
    index = 1
    while index * index <= current:
        if current % index == 0:
            found.add(index)
            found.add(current // index)
        index += 1
    return sorted(found)

def get_category_label(value):
    for key in ['low', 'mid', 'high']:
        record = METRIC_CATEGORIES[key]
        if value < record.threshold:
            return record.label
    return 'high'

if __name__ == '__main__':
    sample = 36
    divs = compute_divisors(sample)
    print(divs)
    print(get_category_label(sample))