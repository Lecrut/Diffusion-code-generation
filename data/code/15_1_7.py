def get_penultimate(items):
    if len(items) < 2:
        raise ValueError("List must contain at least two elements")
    return items[-2]

if __name__ == '__main__':
    print(get_penultimate([1, 2, 3, 4]))