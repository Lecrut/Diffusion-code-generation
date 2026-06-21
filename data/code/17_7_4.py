def get_last_entry(data):
    if not data:
        return None
    return data[-1]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = get_last_entry(sample_data)
    print(result)