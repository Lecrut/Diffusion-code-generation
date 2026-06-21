from collections import Counter

def count_name_frequency(names):
    return sorted(Counter(names).items(), key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    sample_names = ['Alice', 'Bob', 'Alice', 'Cindy', 'Bob', 'Alice']
    print(count_name_frequency(sample_names))