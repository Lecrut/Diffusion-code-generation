def average_length(names):
    return sum(len(name) for name in names) / len(names)

def longer_than_average(names):
    avg = average_length(names)
    return [name for name in names if len(name) > avg]

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    result = longer_than_average(sample_names)
    print(result)