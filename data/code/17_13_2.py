def get_last_entry(data):
    if not data:
        return None
    items = list(data.items())
    return items[-1]

if __name__ == '__main__':
    sample_dict = {"first": 10, "second": 20, "third": 30}
    result = get_last_entry(sample_dict)
    print(result)