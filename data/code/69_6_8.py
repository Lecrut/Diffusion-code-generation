FEET_PER_MILE = 5280

def miles_to_feet(distance_in_miles):
    total_feet = distance_in_miles * FEET_PER_MILE
    return total_feet

def run_samples():
    test_cases = [0, 1, 5, 10.5]
    results = []
    for miles in test_cases:
        feet = miles_to_feet(miles)
        results.append(feet)
    return results

if __name__ == '__main__':
    sample_results = run_samples()
    for value in sample_results:
        print(value)