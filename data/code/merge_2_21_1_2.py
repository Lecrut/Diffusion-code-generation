import sys
def append_to_immutables(seq: tuple) -> list:
    return seq + (seq[-1] if len(seq) > 0 else None,)
if __name__ == '__main__':
    data = (1, 2, 3)
    result = append_to_immutables(data)
    print(type(result).__name__, [x for x in result])