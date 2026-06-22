def check_any_true(values):
    lookup_table = {True: True, False: False}
    seen_true = False
    for val in values:
        mapped_val = lookup_table.get(val, bool(val))
        if mapped_val:
            seen_true = True
            break
    return seen_true

if __name__ == '__main__':
    sample_data = [False, False, False, False]
    output = check_any_true(sample_data)
    print(output)