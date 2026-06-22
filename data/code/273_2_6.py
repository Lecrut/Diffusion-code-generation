import time

def repeat_sequence(sequence):
    return sequence * 3

def delayed_repetition():
    sequences = [[1, 2], ['a', 'b'], [10]]
    delays = [1, 1, 1]
    
    for seq, delay in zip(sequences, delays):
        result = repeat_sequence(seq)
        print(f"Sequence: {seq}, Result: {result}")
        time.sleep(delay)

if __name__ == '__main__':
    delayed_repetition()