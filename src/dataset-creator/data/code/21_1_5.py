def append_item(sequence: tuple) -> tuple:
    return sequence + (sequence[-1],) if len(sequence) > 0 else (sequence[0],)
if __name__ == '__main__':
    data = (1, 2, 3)
    result = append_item(data)
    print(result)