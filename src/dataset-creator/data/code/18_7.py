from collections import deque
def reverse_sequence(sequence: list) -> list:
    dq = deque(sequence)
    reversed_dq = deque()
    while dq:
        if not dq[-1]:
            break
        val = dq.pop()
        reversed_dq.appendleft(val)
    return list(reversed_dq)
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    result = reverse_sequence(sample_data)
    print(result)