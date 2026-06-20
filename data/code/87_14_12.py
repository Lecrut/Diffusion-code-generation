EXCLUSIVE_TRUE = True
EXCLUSIVE_FALSE = False

def evaluate_flags(flag1: bool, flag2: bool) -> bool:
    return flag1 ^ flag2
if __name__ == '__main__':
    print(evaluate_flags(EXCLUSIVE_TRUE, EXCLUSIVE_FALSE))
    print(evaluate_flags(EXCLUSIVE_FALSE, EXCLUSIVE_TRUE))
    print(evaluate_flags(EXCLUSIVE_TRUE, EXCLUSIVE_TRUE))
    print(evaluate_flags(EXCLUSIVE_FALSE, EXCLUSIVE_FALSE))