def run_length_encode(t):
    if not t:
        return {}
    result = {}
    current = t[0]
    count = 1
    for item in t[1:]:
        if item == current:
            count += 1
        else:
            result[current] = count
            current = item
            count = 1
    result[current] = count
    return result

if __name__ == '__main__':
    sample_tuple = (1, 1, 2, 2, 2, 3, 1, 1, 1, 1)
    print(run_length_encode(sample_tuple))