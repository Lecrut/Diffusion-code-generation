def get_value(data: dict, key) -> any:
    return data.get(key)
if __name__ == '__main__':
    stored_data = {'alpha': 10, 'beta': 20, 'gamma': 30}
    result_alpha = get_value(stored_data, 'alpha')
    result_beta = get_value(stored_data, 'nonexistent_key')
    print(f"Alpha: {result_alpha}, Beta: {result_beta}")