def average_length(names):
    if not names:
        return 0
    total_length = sum(len(name) for name in names)
    return total_length / len(names)

def longer_than_average(names):
    avg_length = average_length(names)
    return [name for name in names if len(name) > avg_length]

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "Dave"]
    result = longer_than_average(sample_names)
    print(result)