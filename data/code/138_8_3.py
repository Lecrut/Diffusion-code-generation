if __name__ == '__main__':
    P_values = [0, 1]
    Q_values = [0, 1]
    R_values = [0, 1]
    print("Truth Table for (P OR Q) AND (NOT R)")
    print("-" * 40)
    for p in P_values:
        for q in Q_values:
            for r in R_values:
                p_or_q = p or q
                not_r = not r
                result = p_or_q and not_r
                print(f"P={p}, Q={q}, R={r} -> Result={result}")