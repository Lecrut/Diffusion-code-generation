import time
def simulate_sequence(operations, repetitions):
    start_time = time.perf_counter()
    for _ in range(repetitions):
        for op in operations:
            if op == 'A':
                pass
            elif op == 'B':
                pass
            elif op == 'C':
                pass
            else:
                pass
    end_time = time.perf_counter()
    return end_time - start_time
if __name__ == '__main__':
    sequence = ['A', 'B', 'C']
    repetitions = 100000
    simulation_time = simulate_sequence(sequence, repetitions)
    print(f"Simulation time: {simulation_time:.6f} seconds")