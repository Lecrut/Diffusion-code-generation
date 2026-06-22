def get_third_item(seq):
    if len(seq) < 3:
        raise ValueError("Sequence must have at least three items")
    return seq[2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_third_item(sample_list)
    print(result)