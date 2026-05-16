if __name__ == '__main__':
    p_values = [0, 1]
    q_values = [0, 1]
    r_values = [0, 1]
    print("P | Q | R | (P OR Q) AND (NOT R)")
    print("-" * 40)
    for p in p_values:
        for q in q_values:
            for r in r_values:
                p_or_q = p or q
                not_r = not r
                result = p_or_q and not_r
                print(f"{p} | {q} | {r} | {result}")