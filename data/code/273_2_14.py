import time

def repeat_sequence(sequence):
    for _ in range(3):
        print(sequence)
        time.sleep(1)

if __name__ == '__main__':
    sample_sequence = [1, 2, 3]
    repeat_sequence(sample_sequence)