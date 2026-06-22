import time
DELAY_SECONDS = 1

def repeat_sequence(sequence):
    for _ in range(3):
        print(sequence)
        time.sleep(DELAY_SECONDS)
if __name__ == '__main__':
    sample_sequence = [1, 2]
    repeat_sequence(sample_sequence)