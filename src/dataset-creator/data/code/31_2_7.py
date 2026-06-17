def map_values(data):
    return {k: data[k] for k in data if isinstance(k, str)}
if __name__ == '__main__':
    sample_data = {'alpha': 10, 'beta': 20.5, 'gamma': True}
    result = map_values(sample_data)
    print(result)