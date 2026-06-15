def simulate_sequence(sequence, operations):
    result = []
    for item in sequence:
        for op in operations:
            if op == 'add':
                result.append(item + 1)
            elif op == 'multiply':
                result.append(item * 2)
            elif op == 'subtract':
                result.append(item - 1)
            else:
                result.append(item)
    return result
if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    sample_operations = ['add', 'multiply', 'subtract']
    simulation_result = simulate_sequence(sample_sequence, sample_operations)
    print(simulation_result)