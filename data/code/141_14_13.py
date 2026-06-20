def truth_table():
    inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    and_results = [a & b for a, b in inputs]
    or_results = [a | b for a, b in inputs]
    not_a_results = [~a for a, _ in inputs]
    not_b_results = [~b for _, b in inputs]
    
    return and_results, or_results, not_a_results, not_b_results

if __name__ == '__main__':
    and_res, or_res, not_a_res, not_b_res = truth_table()
    print(f"AND Results: {and_res}")
    print(f"OR Results: {or_res}")
    print(f"NOT A Results: {not_a_res}")
    print(f"NOT B Results: {not_b_res}")