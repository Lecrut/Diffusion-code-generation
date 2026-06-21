def extend_list(base, extension):
    for item in extension:
        if item not in base:
            base.append(item)

if __name__ == '__main__':
    sample_base = [1, 2, 3]
    sample_extension = [3, 4, 5]
    extend_list(sample_base, sample_extension)
    print(sample_base)