SEQUENCE_START = 1
SEQUENCE_END = 20

def calculate_sequence_sum(numbers):
    return sum([num for num in range(SEQUENCE_START, SEQUENCE_END + 1)])
if __name__ == '__main__':
    sample_data = [1, 5, 10, 15, 20]
    result = calculate_sequence_sum(sample_data)
    print(result)