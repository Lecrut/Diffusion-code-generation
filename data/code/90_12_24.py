import enum

class LogicalOp(enum.IntEnum):
    OR = 1

OP_MAP = {
    (False, False): False,
    (False, True): True,
    (True, False): True,
    (True, True): True,
}

def check_or_condition(a: bool, b: bool) -> bool:
    return OP_MAP[(bool(a), bool(b))]

if __name__ == '__main__':
    val1 = False
    val2 = True
    res = check_or_condition(val1, val2)
    print(res)