from typing import Tuple
is_mutually_exclusive = lambda x: sum(x) == 1
if __name__ == '__main__':
    print(is_mutually_exclusive((True, False, False)))
    print(is_mutually_exclusive((False, True, False)))
    print(is_mutually_exclusive((False, False, True)))
    print(is_mutually_exclusive((True, True, False)))
    print(is_mutually_exclusive((False, True, True)))
    print(is_mutually_exclusive((True, False, True)))
    print(is_mutually_exclusive((False, False, False)))