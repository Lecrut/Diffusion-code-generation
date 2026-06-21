def check_any_match(iterable, match_func):
    result_accumulator = False
    items_processed = 0
    for current_item in iterable:
        items_processed += 1
        is_match = match_func(current_item)
        if is_match:
            result_accumulator = True
            break
    if not result_accumulator and items_processed == 0:
        result_accumulator = False
    return result_accumulator

if __name__ == '__main__':
    data_set = [False, None, 0, [], '', -1]
    checker_func = lambda val: val is not None and val != 0 and val != [] and val != ''
    outcome = check_any_match(data_set, checker_func)
    print(outcome)