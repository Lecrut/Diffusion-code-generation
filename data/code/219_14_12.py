def max_from_generator(gen):
    return max(gen)

if __name__ == '__main__':
    sample_gen = (x * x for x in range(10))
    print(max_from_generator(sample_gen))