def max_generator(gen):
    return max(gen)

if __name__ == '__main__':
    sample_gen = (x for x in range(10))
    print(max_generator(sample_gen))