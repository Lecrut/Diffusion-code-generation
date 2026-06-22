def find_min_max(gen):
    min_val = max_val = next(gen)
    for val in gen:
        if val < min_val:
            min_val = val
        elif val > max_val:
            max_val = val
    return min_val, max_val

if __name__ == '__main__':
    sample_gen = (x**2 for x in range(10))
    print(find_min_max(sample_gen))