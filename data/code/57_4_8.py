COUNT_FIBS = 200

def generate_fibonacci(count):
    if count <= 0:
        return []
    terms = [0]
    next_val = 1
    for _ in range(count - 1):
        terms.append(next_val)
        next_val, terms[-1] = terms[-1], terms[-1] + next_val
    return terms

if __name__ == '__main__':
    print(generate_fibonacci(COUNT_FIBS))