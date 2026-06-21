def calculate_expression(a, b, c, d):
    return (a or b) and (c or d)

if __name__ == '__main__':
    for a in [False, True]:
        for b in [False, True]:
            for c in [False, True]:
                for d in [False, True]:
                    result = calculate_expression(a, b, c, d)
                    print(f"A={a}, B={b}, C={c}, D={d}, Result={(result)}")