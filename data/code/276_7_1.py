def simulate_sequence(sequence, repetitions):
    result = []
    for _ in range(repetitions):
        current_sequence = []
        for operation in sequence:
            if operation == 'add':
                current_sequence.append(1)
                current_sequence.append(2)
            elif operation == 'subtract':
                current_sequence.append(-1)
                current_sequence.append(-2)
            elif operation == 'multiply':
                current_sequence.append(3)
                current_sequence.append(4)
            else:
                current_sequence.append(0)
        result.extend(current_sequence)
    return result
if __name__ == '__main__':
    sample_sequence = ['add', 'subtract', 'multiply', 'other']
    sample_repetitions = 3
    simulation_result = simulate_sequence(sample_sequence, sample_repetitions)
    print(simulation_result)