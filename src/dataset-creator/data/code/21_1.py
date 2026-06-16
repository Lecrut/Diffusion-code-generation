def append_to_sequence(seq: tuple) -> tuple:
    return seq + (seq[-1],) if len(seq) > 0 else (*seq,)
if __name__ == '__main__':
    data = (1, 2, 3)
    result = append_to_sequence(data)
    print(result)