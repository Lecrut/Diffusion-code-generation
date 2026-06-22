def min_max_gen(gen):
    try:
        min_val = max_val = next(gen)
        for val in gen:
            if val < min_val:
                min_val = val
            elif val > max_val:
                max_val = val
        return (min_val, max_val)
    except StopIteration:
        raise ValueError('Generator is empty')
if __name__ == '__main__':
    sample_gen = (x for x in range(10))
    print(min_max_gen(sample_gen))