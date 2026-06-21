from collections import Counter

def count_name_frequency(names):
    name_counts = Counter(names)
    return sorted(name_counts.items(), key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    sample_names = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Bob']
    result = count_name_frequency(sample_names)
    print(result)