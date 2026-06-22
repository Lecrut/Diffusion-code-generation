def swap_first_last(s):
    if len(s) < 2:
        return s
    first_char = s[0]
    last_char = s[-1]
    middle_part = s[1:-1]
    return last_char + middle_part + first_char

if __name__ == '__main__':
    sample_values = ["hello", "a", "", "xy", "racecar"]
    for value in sample_values:
        print(swap_first_last(value))