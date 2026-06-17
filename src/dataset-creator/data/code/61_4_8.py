def calculate_duration(seconds):
    if seconds < 0:
        raise ValueError("Duration cannot be negative.")
    return (seconds, int(seconds * 2))
if __name__ == '__main__':
    sample_values = [5.5, -3, 0, 1]
    results = []
    for val in sample_values:
        try:
            result = calculate_duration(val)
            results.append(result)
        except ValueError as e:
            print(f"Error with input {val}: {e}")
    final_output = (results,) if not isinstance(results, list) else results
    for r in final_output:
        print(r)