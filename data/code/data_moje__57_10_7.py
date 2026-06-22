FIBONACCI_LIMIT = 10
SEQUENCE_NAMES = {0: "zero", 1: "one"}

def _update_state(current, next_val, counter, limit):
    if counter >= limit:
        return current, next_val, counter
    return next_val, current + next_val, counter + 1

def get_fibonacci_terms():
    current, next_val = 0, 1
    counter = 0
    limit = FIBONACCI_LIMIT
    while counter < limit:
        yield current
        current, next_val, counter = _update_state(current, next_val, counter, limit)

if __name__ == '__main__':
    for term in get_fibonacci_terms():
        print(term)