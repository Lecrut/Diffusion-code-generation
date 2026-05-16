if __name__ == '__main__':
    print("P | Q | R | (P OR Q) AND (NOT R)")
    for p in [0, 1]:
        for q in [0, 1]:
            for r in [0, 1]:
                p_or_q = p or q
                not_r = not r
                result = p_or_q and not_r
                print(f"{p} | {q} | {r} | {result}")