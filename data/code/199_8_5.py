from collections import Counter

def count_names_frequency(names):
    return sorted(Counter(names).items(), key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    sample_names = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice']
    print(count_names_frequency(sample_names))