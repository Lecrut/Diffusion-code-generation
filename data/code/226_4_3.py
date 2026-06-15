def repeat_sequence(start, factor):
    sequence = [str(start)] * factor
    print(" ".join(sequence))
if __name__ == '__main__':
    repeat_sequence(5, 3)
    repeat_sequence(10, 4)