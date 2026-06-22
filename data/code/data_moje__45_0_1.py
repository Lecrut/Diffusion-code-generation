def find_minimum(values):
    if not values:
        return None
    return min(values)

if __name__ == '__main__':
    sample_data = [5, 2, 9, 1, 7]
    result = find_minimum(sample_data)
    print(result)