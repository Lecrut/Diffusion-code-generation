def fetch_tail_element(data):
    if not data:
        return None
    return next(reversed(data))

if __name__ == '__main__':
    sample = ['alpha', 'beta', 'gamma', 'delta']
    print(fetch_tail_element(sample))