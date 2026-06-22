def retrieve_penultimate(items):
    if not items:
        return None
    return items[-2]

if __name__ == '__main__':
    DATA = ["alpha", "bravo", "charlie", "delta", "echo"]
    print(retrieve_penultimate(DATA))