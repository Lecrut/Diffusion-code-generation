# Check if 'a' is greater than 'b' using a one-line comparison expression with sample values
if __name__ == '__main__':
    a = 10
    b = 5
    result_a_greater_than_b = (a > b) and print(f"{a} is greater than {b}") or ("Not greater" if not (a > b) else "")