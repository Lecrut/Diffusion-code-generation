def analyze_simple_inputs(data):
    true_count = 0
    false_count = 0
    for condition, value in data:
        if condition:
            true_count += 1
        else:
            false_count += 1
    return {"True": true_count, "False": false_count}
if __name__ == '__main__':
    sample_data = [
        (True, 10),
        (False, 20),
        (True, 30),
        (False, 40),
        (True, 50),
        (False, 60),
        (True, 70)
    ]
    results = analyze_simple_inputs(sample_data)
    print(results)