def and_truth_table():
    a = False
    b = False
    print("A | B | A AND B")
    print("-----------------")
    if a and b:
        print(f"{'False'}|{'False'}|{'True'}")
    elif a and not b:
        print(f"{'False'}|{'True'}|{'False'}")
    elif not a and b:
        print(f"{'True'}|{'False'}|{'False'}")
    else:
        print(f"{'True'}|{'True'}|{'False'}")
if __name__ == '__main__':
    and_truth_table()