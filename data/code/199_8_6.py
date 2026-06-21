from collections import Counter

def count_name_frequency(names):
    if not isinstance(names, list) or not all(isinstance(name, str) for name in names):
        raise ValueError("Input must be a list of strings")
    
    name_counts = Counter(names)
    return sorted(name_counts.items(), key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    sample_names = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Bob']
    print(count_name_frequency(sample_names))