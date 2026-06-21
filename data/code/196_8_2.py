def extend_list(base, extension):
    base.extend(extension)

if __name__ == '__main__':
    sample_base = [1, 2, 3]
    sample_extension = [4, 5, 6]
    extend_list(sample_base, sample_extension)
    print(sample_base)