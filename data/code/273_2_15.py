import time

def repeat_sequence(sequence):
    for _ in range(3):
        print(sequence)
        time.sleep(1)

if __name__ == '__main__':
    sequence1 = [1, 2]
    sequence2 = ['a', 'b']
    sequence3 = [10]

    repeat_sequence(sequence1)
    repeat_sequence(sequence2)
    repeat_sequence(sequence3)