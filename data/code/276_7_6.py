def simulate_sequence(sequence, repetitions):
    result = []
    for _ in range(repetitions):
        current_run = []
        for operation in sequence:
            if operation == 'A':
                current_run.append(1)
            elif operation == 'B':
                current_run.append(2)
            elif operation == 'C':
                current_run.append(3)
            else:
                current_run.append(0)
        result.extend(current_run)
    return result
if __name__ == '__main__':
    sample_sequence = ['A', 'B', 'C', 'A']
    sample_repetitions = 5
    simulation_result = simulate_sequence(sample_sequence, sample_repetitions)
    print(simulation_result)