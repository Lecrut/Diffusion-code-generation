def check_booleans(a: bool, b: bool) -> None:
    if a and b:
        print("Both booleans are true.")
    else:
        print("At least one boolean is false.")

if __name__ == '__main__':
    check_booleans(True, True)
    check_booleans(False, True)
    check_booleans(True, False)
    check_booleans(False, False)