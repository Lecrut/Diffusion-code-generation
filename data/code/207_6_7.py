def max_generator(gen):
    return max(gen)

if __name__ == '__main__':
    sample_gen = (x for x in [3, 5, 1, 2, 4])
    print(max_generator(sample_gen))