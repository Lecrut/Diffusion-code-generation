def average(sequence):
    try:
        return sum(x for x in sequence) / len(sequence)
    except TypeError:
        raise ValueError("Input is not iterable")
    except ZeroDivisionError:
        raise ValueError("Empty sequence")

if __name__ == '__main__':
    sample_sequence = [10, 20, 30, 40, 50]
    print(average(sample_sequence))