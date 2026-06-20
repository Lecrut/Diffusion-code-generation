def check_logic(A, B, C):
    return A and (B or not C)

if __name__ == '__main__':
    TRUE = True
    FALSE = False
    results = [
        check_logic(TRUE, TRUE, FALSE),
        check_logic(TRUE, FALSE, TRUE),
        check_logic(FALSE, TRUE, FALSE),
        check_logic(FALSE, FALSE, TRUE)
    ]
    print(results)