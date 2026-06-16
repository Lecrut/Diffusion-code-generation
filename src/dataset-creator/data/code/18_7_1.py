from collections import deque
def reverse_sequence(sequence):
    return deque(reversed(list(sequence)))
if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    reversed_data = reverse_sequence(data)
    print(list(reversed_data))