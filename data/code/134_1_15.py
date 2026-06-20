MUTUAL_EXCLUSIVE_FLAG = 1

def are_mutually_exclusive(flags: int) -> bool:
    return flags & flags - 1 == 0 and flags != 0
if __name__ == '__main__':
    flags1 = MUTUAL_EXCLUSIVE_FLAG << 0
    print(f'Test Case 1: {are_mutually_exclusive(flags1)}')
    flags2 = MUTUAL_EXCLUSIVE_FLAG << 1
    print(f'Test Case 2: {are_mutually_exclusive(flags2)}')
    flags3 = MUTUAL_EXCLUSIVE_FLAG << 0 | MUTUAL_EXCLUSIVE_FLAG << 1
    print(f'Test Case 3: {are_mutually_exclusive(flags3)}')