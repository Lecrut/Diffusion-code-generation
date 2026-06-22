def check_any_true(values):
    truth_map = {True: 1, False: 0}
    return any(v in truth_map and truth_map[v] == 1 for v in values)

if __name__ == '__main__':
    sample_list = [False, True, False, False]
    answer = check_any_true(sample_list)
    print(answer)