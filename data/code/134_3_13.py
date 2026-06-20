from typing import Tuple
check_mutual_exclusivity = lambda x: sum(x) == 1
if __name__ == '__main__':
    print(check_mutual_exclusivity((True, False, False)))
    print(check_mutual_exclusivity((False, True, False)))
    print(check_mutual_exclusivity((False, False, True)))
    print(check_mutual_exclusivity((True, True, False)))
    print(check_mutual_exclusivity((False, True, True)))
    print(check_mutual_exclusivity((True, False, True)))