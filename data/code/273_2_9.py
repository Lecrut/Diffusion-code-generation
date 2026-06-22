import time
REPEAT_COUNT = 3
DELAY_SECONDS = 1

def repeat_sequence(sequence):
    for _ in range(REPEAT_COUNT):
        print(sequence)
        time.sleep(DELAY_SECONDS)
if __name__ == '__main__':
    sequence1 = [1, 2]
    repeat_sequence(sequence1)
    sequence2 = ['a', 'b']
    repeat_sequence(sequence2)
    sequence3 = [10]
    repeat_sequence(sequence3)