min_value = lambda lst: min(lst) if lst else None

if __name__ == '__main__':
    samples = {
        'sample1': [3, 1, 4, 1, 5],
        'sample2': [7],
        'sample3': []
    }
    
    for name, sample in samples.items():
        print(f"Minimum in {name}: {min_value(sample)}")