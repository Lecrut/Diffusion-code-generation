def check_true_presence(values):
    if not values:
        return False
    return any(values)

if __name__ == '__main__':
    sample_values = [True, False, False, False]
    result = check_true_presence(sample_values)
    print(result)