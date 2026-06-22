def validate_limit(limit):
    if not isinstance(limit, int) or limit <= 0:
        raise ValueError("Limit must be a positive integer")

def growing_sequence(limit):
    validate_limit(limit)
    return (x for x in range(1, limit + 1))

if __name__ == '__main__':
    for number in growing_sequence(5):
        print(number)