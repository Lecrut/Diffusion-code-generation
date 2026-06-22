def get_last_entry(items):
    if not items:
        return None
    return items[-1]

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    result = get_last_entry(sample_data)
    print(result)