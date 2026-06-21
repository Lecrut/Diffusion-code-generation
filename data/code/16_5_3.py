def get_initial_value(values):
    if not values:
        return None
    return values[0]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_initial_value(sample_list)
    print(result)