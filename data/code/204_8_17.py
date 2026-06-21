def find_middle(data):
    if not data:
        return None
    n = len(data)
    return data[n // 2]

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    print(find_middle(sample_data))