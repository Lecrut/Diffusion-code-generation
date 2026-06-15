def repeat_sequence(start, factor):
    sequence = [start]
    for _ in range(factor):
        sequence.extend([start] * factor)
    print(" ".join(map(str, sequence)))
if __name__ == '__main__':
    repeat_sequence(5, 3)
    repeat_sequence(10, 2)
    repeat_sequence(1, 4)