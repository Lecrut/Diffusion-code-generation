import matplotlib.pyplot as plt
def generate_sequence(n):
    sequence = []
    if n <= 0:
        return sequence
    a1 = 1
    sequence.append(a1)
    diff = 1
    for i in range(2, n + 1):
        next_term = sequence[-1] + diff
        sequence.append(next_term)
        diff += 1
    return sequence
if __name__ == '__main__':
    N = 10
    sequence_values = generate_sequence(N)
    x_values = list(range(1, N + 1))
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, sequence_values, marker='o', linestyle='-', color='b')
    plt.title('Sequence where differences increase by 1')
    plt.xlabel('Term Number (n)')
    plt.ylabel('Sequence Value')
    plt.grid(True)
    plt.show()