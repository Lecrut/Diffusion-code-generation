def group_by_length(strings):
    return {len(s): [s for s in strings if len(s) == k] for k in set(len(s) for s in strings)}

if __name__ == '__main__':
    sample_strings = ["alpha", "beta", "gamma", "delta"]
    grouped_by_length = group_by_length(sample_strings)
    print(grouped_by_length)