def and_truth_table():
    a = False
    b = False
    print("A | B | A AND B")
    print("-----------------")
    if a:
        if b:
            result = True
        else:
            result = False
    else:
        result = False
    print(f"{a} | {b} | {result}")
if __name__ == '__main__':
    and_truth_table()