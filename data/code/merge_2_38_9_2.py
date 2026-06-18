def memory_efficient_generator(source_iter):
    for key in source_iter:
        yield key, f"value_for_{key}"
if __name__ == '__main__':
    data = ['alpha', 'beta', 'gamma']
    result_dict = {}
    generator = memory_efficient_generator(data)
    while True:
        try:
            k_v_pair = next(generator)
            result_dict[k_v_pair[0]] = k_v_pair[1]
        except StopIteration:
            break
    print(result_dict)