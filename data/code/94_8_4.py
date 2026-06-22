TRUE_MAP = {'true': True, 'false': False}

def contains_truth(values):
    if not values:
        return False
    return any(values)

if __name__ == '__main__':
    sample_data = [False, False, True, False]
    output = contains_truth(sample_data)
    print(output)