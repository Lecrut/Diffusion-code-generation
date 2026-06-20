def validate_truth_table():
    for A in [0, 1]:
        for B in [0, 1]:
            result = (A and B) or (not A and not B)
            if not result:
                return False
    return True

if __name__ == '__main__':
    print(validate_truth_table())