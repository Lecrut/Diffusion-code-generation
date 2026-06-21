import random
import operator

def extract_random_from_set(source_set):
    if not source_set:
        return None
    items = list(source_set)
    count = len(items)
    index = random.randrange(count)
    return operator.getitem(items, index)

if __name__ == '__main__':
    sample_collection = {10, 20, 30, 40}
    picked_value = extract_random_from_set(sample_collection)
    print(picked_value)