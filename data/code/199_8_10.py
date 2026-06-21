from collections import Counter

def count_name_frequency(names):
    name_counter = Counter(names)
    sorted_names = sorted(name_counter.items(), key=lambda x: x[1], reverse=True)
    return sorted_names

if __name__ == '__main__':
    sample_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Alice', 'Bob']
    result = count_name_frequency(sample_names)
    print(result)