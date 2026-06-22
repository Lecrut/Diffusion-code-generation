import time

class SequenceRepeater:
    DELAY = 1
    
    @staticmethod
    def repeat(sequence, count):
        if count <= 0:
            return []
        result = []
        for _ in range(count):
            result.extend(sequence)
            time.sleep(SequenceRepeater.DELAY)
        return result

if __name__ == '__main__':
    repeater = SequenceRepeater()
    sequence1 = [1, 2]
    count1 = 3
    result1 = repeater.repeat(sequence1, count1)
    print(f"Sequence: {sequence1}, Count: {count1}")
    print(f"Result: {result1}")
    
    sequence2 = ['a', 'b']
    count2 = 4
    result2 = repeater.repeat(sequence2, count2)
    print(f"Sequence: {sequence2}, Count: {count2}")
    print(f"Result: {result2}")