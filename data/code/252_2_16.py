def compare_two_simple_quantities_now_batch_process(values: list) -> list:
    results = []
    for a, b in values:
        difference = a - b
        if difference > 0:
            result_type = 'greater'
        elif difference < 0:
            result_type = 'less'
        else:
            result_type = 'equal'
        results.append({
            "a": a,
            "b": b,
            "comparison_result": f"a is {result_type} than b"
        })
    return results

if __name__ == '__main__':
    sample_values = [(10, 5), (20, 20), (30, 40)]
    comparison_results = compare_two_simple_quantities_now_batch_process(sample_values)
    for result in comparison_results:
        print(result)