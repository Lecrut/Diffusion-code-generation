def evaluate_expression(p, q):
    p_val = bool(p)
    q_val = bool(q)
    result = (p_val and q_val)
    return result
if __name__ == '__main__':
    print("P | Q | P AND Q")
    print("---|---|---------")
    p_values = [False, True]
    q_values = [False, True]
    for p in p_values:
        for q in q_values:
            result = evaluate_expression(p, q)
            print(f"{str(p).ljust(2)} | {str(q).ljust(2)} | {str(result)}")