def run_length_encode(values):
    if not values:
        return []
    result = []
    current = values[0]
    count = 1
    for v in values[1:]:
        if v == current:
            count += 1
        else:
            result.append((current, count))
            current = v
            count = 1
    result.append((current, count))
    return result

if __name__ == '__main__':
    sample = [1, 1, 2, 3, 3, 3, 4, 4, 5]
    print(run_length_encode(sample))