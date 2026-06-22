import time

def repeat_sequence(sequence):
    for _ in range(3):
        print(f"Sequence: {sequence}")
        time.sleep(1)

if __name__ == '__main__':
    sequence1 = [1, 2]
    repeat_sequence(sequence1)
    
    sequence2 = ['a', 'b']
    repeat_sequence(sequence2)
    
    sequence3 = [10, 20, 30]
    repeat_sequence(sequence3)