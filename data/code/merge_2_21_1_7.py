import sys
def append_to_sequence(seq: tuple) -> list:
    return seq + (seq[-1],) if len(seq) > 0 else [None]
if __name__ == '__main__':
    sample = (1, 2, 3)
    result = append_to_sequence(sample)
    print(type(result), list(result))