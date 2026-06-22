MIN_LENGTH_KEY = 'length'

def min_by_length(strings):
    return min(strings, key=lambda x: (len(x), x))

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry", "date"]
    print(min_by_length(sample_values))