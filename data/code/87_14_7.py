FLAG_TRUE = True
FLAG_FALSE = False

def exclusive_truthiness(flag1: bool, flag2: bool) -> bool:
    return flag1 ^ flag2
if __name__ == '__main__':
    print(exclusive_truthiness(FLAG_TRUE, FLAG_FALSE))
    print(exclusive_truthiness(FLAG_FALSE, True))
    print(exclusive_truthiness(FLAG_TRUE, True))
    print(exclusive_truthiness(FLAG_FALSE, FLAG_FALSE))