import matplotlib.pyplot as plt
def generate_sequence(n):
    sequence = []
    if n <= 0:
        return sequence
    a1 = 1
    sequence.append(a1)
    current_diff = 1
    for i in range(2, n + 1):
        next_term = sequence[-1] + current_diff
        sequence.append(next_term)
        current_diff += 1
    return sequence
if __name__ == '__main__':
    N = 10
    sequence = generate_sequence(N)
    x_values = list(range(1, N + 1))
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, sequence, marker='o', linestyle='-', color='b')
    plt.title('Sequence with Increasing Differences')
    plt.xlabel('Term Number (n)')
    plt.ylabel('Sequence Value')
    plt.grid(True)
    plt.xticks(x_values)
    plt.tight_layout()
    plt.show()