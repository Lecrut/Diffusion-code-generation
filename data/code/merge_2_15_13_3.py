import random
def sort_integers(data):
    return sorted(data)
def sort_floats(data):
    return sorted(data, key=lambda x: float(x)) if any(not isinstance(x, (int, float)) for x in data) else sorted(data)
def process_large_dataset():
    sample_integers = [random.randint(-10**6, 10**6) for _ in range(5000)]
    sample_floats = [round(random.uniform(-1.0e4, 1.0e4), 2) for _ in range(5000)]
    sorted_integers = sort_integers(sample_integers.copy())
    sorted_floats = sort_floats(sample_floats.copy())
    return {
        'integers': sorted_integers[:5],
        'floats': sorted_floats[:5]
    }
if __name__ == '__main__':
    result = process_large_dataset()
    print(f"Sample Sorted Integers: {result['integers']}")
    print(f"Sample Sorted Floats: {result['floats']}")