import sys
def simulate_sequence(sequence, repetitions):
    result = []
    for _ in range(repetitions):
        current_sequence = []
        for operation in sequence:
            if operation == 'A':
                current_sequence.append(1)
            elif operation == 'B':
                current_sequence.append(2)
            elif operation == 'C':
                current_sequence.append(3)
            else:
                current_sequence.append(0)
        result.extend(current_sequence)
    return result
if __name__ == '__main__':
    SEQUENCE = ['A', 'B', 'C', 'A']
    REPETITIONS = 1000
    simulation_result = simulate_sequence(SEQUENCE, REPETITIONS)
    print(f"Total length of simulated sequence: {len(simulation_result)}")