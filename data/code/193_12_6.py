def aggregate_values(data):
    return sum(filter(lambda x: isinstance(x, (int, float)), data))

if __name__ == '__main__':
    sample_data = [10, 25, 'a', None, 30.5, 5]
    total = aggregate_values(sample_data)
    print(total)