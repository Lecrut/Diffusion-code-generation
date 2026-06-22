def validate_boundaries(limit):
    if limit < 0 or limit > 99:
        raise ValueError("Limit must be between 0 and 99 inclusive.")

def print_growing_sequence(limit):
    validate_boundaries(limit)
    i = 0
    while i <= limit:
        print(i)
        i += 1

if __name__ == '__main__':
    sample_limit = 50
    print_growing_sequence(sample_limit)