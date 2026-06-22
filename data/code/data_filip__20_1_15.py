def run_length_encode(integers):
    if not integers:
        return []
    encoded = []
    current_value = integers[0]
    count = 1
    for i in range(1, len(integers)):
        if integers[i] == current_value:
            count += 1
        else:
            encoded.append((current_value, count))
            current_value = integers[i]
            count = 1
    encoded.append((current_value, count))
    return encoded

if __name__ == '__main__':
    sample_integers = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4]
    result = run_length_encode(sample_integers)
    print(result)