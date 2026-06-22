def check_boolean_uniformity(values):
    if not values:
        return True
    target = values[0]
    for value in values:
        if value != target:
            return False
    return True

if __name__ == '__main__':
    sample_data = [False, False, False]
    result = check_boolean_uniformity(sample_data)
    print(result)