def compare_elements(list_one, list_two):
    if len(list_one) != len(list_two):
        raise ValueError("Lists must be of equal length")
    results = []
    for x, y in zip(list_one, list_two):
        if x < y:
            results.append(f"{x} < {y}")
        elif x > y:
            results.append(f"{x} > {y}")
        else:
            results.append(f"{x} == {y}")
    return results

if __name__ == '__main__':
    sample_a = [10, 20, 30, 40]
    sample_b = [10, 25, 25, 40]
    result = compare_elements(sample_a, sample_b)
    for line in result:
        print(line)