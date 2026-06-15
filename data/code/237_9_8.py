import matplotlib.pyplot as plt
def generate_sequence(n):
    sequence = []
    if n <= 0:
        return sequence
    sequence.append(1)
    current_diff = 1
    for i in range(1, n):
        current_diff += 1
        next_term = sequence[-1] + current_diff
        sequence.append(next_term)
    return sequence
def visualize_sequence(n):
    terms = generate_sequence(n)
    x_values = list(range(1, n + 1))
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, terms, marker='o', linestyle='-', color='b')
    plt.title('Sequence where difference increases by 1')
    plt.xlabel('Term Number (n)')
    plt.ylabel('Sequence Value')
    plt.grid(True)
    plt.xticks(x_values)
    plt.yscale('log')
    plt.show()
if __name__ == '__main__':
    N = 10
    visualize_sequence(N)