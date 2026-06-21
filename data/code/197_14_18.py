def is_subset(subset, master):
    if not isinstance(subset, list) or not isinstance(master, list):
        raise ValueError("Both arguments must be lists.")
    return all(item in master for item in subset)

if __name__ == '__main__':
    group_a = [101, 102, 103, 104, 105]
    group_b = [104, 105, 106, 107, 108]
    print(f"Is group A a subset of group B? {is_subset(group_a, group_b)}")