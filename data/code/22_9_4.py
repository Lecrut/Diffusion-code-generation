import time

def is_odd_bitwise(n: int) -> bool:
    """Check if an integer is odd using bitwise operations."""
    return n & 1 != 0

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or arguments.
    samples = [2, 3, -5, 7, 8]

    print("Testing odd check using bitwise AND with 1:")
    for val in samples:
        start_time = time.perf_counter_ns()
        result = is_odd_bitwise(val)
        end_time = time.perf_counter_ns()
        
        duration_ms = (end_time - start_time) / 1_000_000

        if val % 2 != 0:
            status_ok = "Correct"
        else:
            status_ok = "Incorrect"

        print(f"{val}: {result} ({status_ok}) | Bitwise check took {duration_ms:.6f} ms")