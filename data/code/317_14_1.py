def generate_cycle(min_val, max_val):
    return [i for i in range(min_val, max_val + 1)]
if __name__ == '__main__':
    min_bound = 3
    max_bound = 7
    result = generate_cycle(min_bound, max_bound)
    print(result)