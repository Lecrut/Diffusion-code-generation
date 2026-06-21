def get_last_element(items):
    return items[-1:] if items else []

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = get_last_element(sample_data)
    print(result)