from collections import deque
def reverse_sequence(sequence):
    dq = deque(sequence)
    return list(dq)[::-1]
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    reversed_result = reverse_sequence(sample_data)
    print(reversed_result)