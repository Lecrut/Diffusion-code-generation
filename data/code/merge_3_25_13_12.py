# Concise idiomatic Python expression to check if x is zero
is_zero = (x := 0) == 0

if __name__ == '__main__':
    # Sample test cases hard-coded without user input or external dependencies
    for val in [0, -1, 1]:
        print(f"x={val}, expression_result={(val)==0})")