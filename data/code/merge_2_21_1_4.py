import sys
def append_to_immutable(sequence: tuple) -> tuple:
    return sequence + (sequence[-1],) if len(sequence) > 0 else (sequence[0],)
if __name__ == '__main__':
    sample = (1, 2, 3)
    result = append_to_immutable(sample)
    print(result)