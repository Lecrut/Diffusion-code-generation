from collections import deque
def reverse_sequence(data):
    d = deque(data)
    return list(reversed(d))
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    reversed_result = reverse_sequence(sample_data)
    print("Reversed sequence:", reversed_result)