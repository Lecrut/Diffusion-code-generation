def compare_two_simple_quantities_now_batch_process(values: list) -> dict:
    if not all(isinstance(v, (int, float)) for v in values):
        raise ValueError("All elements in the list must be numbers")
    if len(values) % 2 != 0:
        raise ValueError("The list must contain an even number of elements")

    results = {}
    for i in range(0, len(values), 2):
        a, b = values[i], values[i + 1]
        if a > b:
            result_message = "a is greater than b"
        elif a < b:
            result_message = "a is less than b"
        else:
            result_message = "a is equal to b"
        results[f"Comparison_{i//2+1}"] = {
            "a": a,
            "b": b,
            "result": result_message
        }
    return results

if __name__ == '__main__':
    sample_values = [5, 3, 8, 8, 10, 7]
    print(compare_two_simple_quantities_now_batch_process(sample_values))