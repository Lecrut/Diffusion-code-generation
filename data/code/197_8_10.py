VALID_MEMBERS = (1, 5, 2, 8, 3)

def is_member(target):
    return target in VALID_MEMBERS

if __name__ == '__main__':
    sample_values = [8, 'z', 25, 1]
    results = {val: is_member(val) for val in sample_values}
    print(results)