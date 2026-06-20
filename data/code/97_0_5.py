def print_truth_table(p: bool, q: bool) -> None:
    if not isinstance(p, bool) or not isinstance(q, bool):
        raise ValueError("Both inputs must be boolean values.")
    
    print(f"P | Q | P AND Q")
    print("---|---|---------")
    p_and_q = p and q
    print(f"{p} | {q} | {p_and_q}")

if __name__ == '__main__':
    try:
        print_truth_table(True, False)
        print_truth_table(False, True)
        print_truth_table(True, True)
        print_truth_table(False, False)
    except ValueError as e:
        print(e)