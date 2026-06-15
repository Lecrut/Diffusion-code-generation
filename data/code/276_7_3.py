def simulate_sequence(operations, repetitions):
    result = []
    for _ in range(repetitions):
        current_sequence = []
        for op in operations:
            if op == 'A':
                current_sequence.append(1)
            elif op == 'B':
                current_sequence.append(2)
            elif op == 'C':
                current_sequence.append(3)
            else:
                raise ValueError("Unknown operation")
        result.extend(current_sequence)
    return result
if __name__ == '__main__':
    sample_operations = ['A', 'B', 'C']
    sample_repetitions = 5
    simulation_result = simulate_sequence(sample_operations, sample_repetitions)
    print(simulation_result)