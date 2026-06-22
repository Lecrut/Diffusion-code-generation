import time

def repeat_sequence(sequence, count):
    for _ in range(count):
        print(sequence)
        time.sleep(1)

if __name__ == '__main__':
    sequence1 = [1, 2]
    count1 = 3
    repeat_sequence(sequence1, count1)
    sequence2 = ['a', 'b']
    count2 = 4
    repeat_sequence(sequence2, count2)
    sequence3 = [10]