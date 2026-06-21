def extend_list(base, extension):
    if not isinstance(base, list) or not isinstance(extension, list):
        raise ValueError("Both inputs must be lists.")
    base.extend(extension)

if __name__ == '__main__':
    sample_base = [1, 2, 3]
    sample_extension = [4, 5, 6]
    extend_list(sample_base, sample_extension)
    print(sample_base)