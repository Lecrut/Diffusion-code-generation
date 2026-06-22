def swap_first_last(s):
    if len(s) < 2:
        return s
    first, last = s[0], s[-1]
    middle = s[1:-1]
    return last + middle + first

if __name__ == '__main__':
    sample_values = ["world", "x", "", "xy", "level"]
    for value in sample_values:
        print(swap_first_last(value))