def find_min_max(gen):
    min_val = max_val = None
    for value in gen:
        if min_val is None or value < min_val:
            min_val = value
        if max_val is None or value > max_val:
            max_val = value
    return (min_val, max_val)

if __name__ == '__main__':
    sample_gen = (x * x for x in range(10))
    print(find_min_max(sample_gen))