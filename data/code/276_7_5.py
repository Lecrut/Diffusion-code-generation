def simulate_sequence(sequence, repetition_count):
    result = []
    for _ in range(repetition_count):
        current_iteration = []
        for operation in sequence:
            if operation == 'add':
                current_iteration.append(1)
            elif operation == 'subtract':
                current_iteration.append(-1)
            elif operation == 'multiply':
                current_iteration.append(2)
            elif operation == 'divide':
                current_iteration.append(0)
            else:
                current_iteration.append(operation)
        result.extend(current_iteration)
    return result
if __name__ == '__main__':
    sequence = ['add', 'subtract', 'multiply', 'divide', 'unknown']
    repetition_count = 5
    simulated_output = simulate_sequence(sequence, repetition_count)
    print(simulated_output)