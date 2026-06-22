from itertools import zip_longest

THRESHOLD_OFFSET = 0

def compare_and_log_greater(list_first, list_second):
    results = []
    for val_a, val_b in zip_longest(list_first, list_second, fillvalue=THRESHOLD_OFFSET):
        if val_a is not None and val_b is not None:
            if val_a > val_b:
                results.append((val_a, val_b))
    return results

if __name__ == '__main__':
    sample_first = [12, 4, 9, 2]
    sample_second = [3, 5, 8, 1]
    matches = compare_and_log_greater(sample_first, sample_second)
    for high, low in matches:
        print(f"{high} > {low}")
    print(f"Total matches: {len(matches)}")