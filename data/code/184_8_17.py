SAMPLE_SEQUENCE = ['apple', 'banana', 'cherry']
TARGET_WORD_1 = 'banana'
TARGET_WORD_2 = 'grape'

def word_exists(sequence, target):
    return any((word == target for word in sequence))
if __name__ == '__main__':
    print(f"Checking if '{TARGET_WORD_1}' exists: {word_exists(SAMPLE_SEQUENCE, TARGET_WORD_1)}")
    print(f"Checking if '{TARGET_WORD_2}' exists: {word_exists(SAMPLE_SEQUENCE, TARGET_WORD_2)}")